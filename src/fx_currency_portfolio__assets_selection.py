#!/usr/bin/python3

"""Currency Portfolio: Assets Selection.

Description:
    Currency Selection in anti-crisis portfolio using monte Carlo simulation.
"""

# %% Import dependencies ----
# core
import sys
import warnings
from IPython import sys_info

# data science
import pandas as pd
import numpy as np
from scipy.stats import norm

# Cloud integration
from azureml.core import Workspace, Dataset, ComputeTarget, VERSION as aml_version
print(f'Azure ML SDK v{aml_version}')
# plots
import matplotlib.pyplot as plt
import seaborn as sns

# show info about python env
print(sys_info())
warnings.filterwarnings("ignore")


# %% Set params ----
symbols = ['USD/CHF', 'USD/CNY', 'USD/EUR', 'USD/GBP', 'USD/HKD', 'USD/JPY', 'USD/KZT', 'USD/RUB']

n_days = int(252)  # US market has 252 trading days in a year
n_simulations = int(1e4)


# %% Connect to Azure ML workspace ----
ws =  Workspace.from_config()
print(f"Connected to *{ws.get_details()['friendlyName']}* workspace in *{ws.get_details()['location']}*.")

print('Compute Targets:')
for compute_name in ws.compute_targets:
    compute = ws.compute_targets[compute_name]
    print('\t', compute.name, ':', compute.type)

# > htop


# %% Load dateset ----
currencies_ds = Dataset.get_by_name(ws, name='Currencies')
currencies_ds.to_pandas_dataframe()

print(f'Dataset name: {currencies_ds.name}. Description: {currencies_ds.description}.')
print(f'Size of Azure ML dataset object: {sys.getsizeof(currencies_ds)} bytes.')


# %% Preprocessing ----

quotes_df = (currencies_ds
    # materialize
    .to_pandas_dataframe()
    # define format
    .rename(columns={'slug': 'symbol'})
    .loc[:, ['symbol', 'date', 'close']]
    # filter
    .query("symbol in @symbols")
    .query("date > '2012-01-01'")
    # set time index
    .set_index('date')
    .sort_values(by='date'))

quotes_df


# %% Discover data ----
quotes_df.groupby('symbol')['close'].agg(['count', 'last'])
  

# %% USD/RUB dataset ----
usdrub_df = quotes_df[quotes_df.symbol == 'USD/RUB']
usdrub_df


# %% Calculate Return ----
def calc_returns(close_prices: pd.Series) -> pd.Series:
    """Calculate Investment Return"""
    return (close_prices/close_prices.shift()) - 1


usdrub_df['diff'] = usdrub_df['close'].diff()
usdrub_df['return'] = calc_returns(usdrub_df['close'])

usdrub_df[['close', 'diff', 'return']].tail(10)


# %% Calculate LogReturn ----
def calc_log_returns(return_prices: pd.Series) -> pd.Series:
    """Calculate Log Return"""
    return np.log(1 + return_prices)

usdrub_df['log_return'] = usdrub_df['return'].apply(lambda x: calc_log_returns(x))
usdrub_df[['close', 'diff', 'return', 'log_return']].tail(10)


# %% Simulate possible LogReturns ----

def calc_simulated_returns(log_returns: pd.Series, n_days: int, n_iterations: int) -> pd.Series:
    """Calculate Simulated Return"""

    u = log_returns.mean()
    var = log_returns.var()
    stdev = log_returns.std()

    drift = u - (0.5*var)
    Z = norm.ppf(np.random.rand(n_days, n_iterations))

    return np.exp(drift + stdev*Z)


usdrub_simulated_returns = calc_simulated_returns(
    usdrub_df['log_return'].dropna(),
    n_days,
    n_simulations)

assert(
    usdrub_simulated_returns.shape == (n_days, n_simulations)
    and (usdrub_simulated_returns > 0).all()
    and (usdrub_simulated_returns < 2).all()
)


# %% Monte carlo simulation evaluation ----

def get_breakeven_prob(pred, risk_free_rate: float = 0.02) -> pd.Series:
    """
    Calculation of the probability of a stock being above a certain threshold,
    which can be defined as a value (final stock price) or return rate (percentage change).
    """

    init_pred = pred.iloc[0, 0]

    last_pred = pred.iloc[-1]
    pred_list = list(last_pred)

    over = [(p*100)/init_pred for p in pred_list if ((p-init_pred)*100)/init_pred >= risk_free_rate]
    less = [(p*100)/init_pred for p in pred_list if ((p-init_pred)*100)/init_pred < risk_free_rate]

    return len(over)/(len(over) + len(less))


def evaluate_simulation(simulated_returns: pd.Series, last_actual_price: float, n_days: int, plot: bool = True) -> pd.DataFrame:
    """
    Evaluate Monte-Carlo simulations result
    """

    # Create empty matrix
    price_list = np.zeros_like(simulated_returns)

    # Put the last actual price in the first row,
    # and calculate the price of each day
    price_list[0] = last_actual_price
    for t in range(1, n_days):
        price_list[t] = price_list[(t - 1)]*simulated_returns[t]

    # convert to temp dataframe
    price_df = pd.DataFrame(price_list)

    # Plot
    if plot == True:
        x = price_df.iloc[-1]
        fig, ax = plt.subplots(1, 2, figsize=(14, 4))
        sns.distplot(x, ax=ax[0])
        sns.distplot(x, hist_kws={'cumulative': True}, kde_kws={'cumulative': True}, ax=ax[1])
        plt.xlabel('Stock Price')
        plt.show()

    print('Results:')
    print(f'\tInvestment period: {n_days-1} days')
    print(f'\tExpected Value: {round(price_df.iloc[-1].mean(), 2)} per USD')
    print(f'\tReturn: {round(100*(price_df.iloc[-1].mean() - price_list[0,1])/price_df.iloc[-1].mean(), 2)}%')
    print(f'\tProbability of Breakeven: {get_breakeven_prob(price_df)}')

    return price_df


# %% Run Monte carlo simulation and estimate result ----

usdrub_mc_simulation_df = evaluate_simulation(
    usdrub_simulated_returns,
    last_actual_price = usdrub_df['close'].tail(1),
    n_days = n_days)


plt.figure(figsize=(10, 6))
plt.plot(usdrub_mc_simulation_df.sample(10, axis='columns'))
plt.title('USD/RUB Price Simulation')
plt.xlabel('Days')
plt.ylabel('RUB per $1')
plt.ylim(10, 300)
plt.show()


# %% Monte Carlo simulation pipeline for multiple tokens ----
# 0. set simulation params
n_simulations = int(1e5)

# 1. prepare
quotes_data = [quotes_df.query('symbol == @s') for s in quotes_df.symbol.unique()]
symbols_list = [df.symbol.unique() for df in quotes_data]

# 2. simulate
returns_data = [calc_returns(df['close']) for df in quotes_data]
log_returns_data = [calc_log_returns(r) for r in returns_data]
simulated_returns_data = [calc_simulated_returns(lr, n_days, n_simulations) for lr in log_returns_data]

assert(
    len(quotes_data) > 0
    and len(quotes_data) == len(symbols_list) == len(returns_data) == len(log_returns_data) == len(simulated_returns_data)
)

# 3. evaluate
for i in range(len(symbols_list)):
    print(f'---- Starting Monte-Carlo simulation for {symbols_list[i]} symbol ----')

    prices_ms = evaluate_simulation(simulated_returns_data[i], quotes_data[i]['close'].tail(1), n_days, plot=False)

    plt.figure(figsize=(10, 6))
    plt.plot(prices_ms.sample(50, axis='columns'))
    plt.title(f'{symbols_list[i]} Price Simulation')
    plt.xlabel('Days')
    plt.ylabel('Amount per $1')
    plt.show()


# %% Completed ----
gc()

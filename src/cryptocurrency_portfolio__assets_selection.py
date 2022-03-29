#!/usr/bin/python3


"""Crypto Currency Portfolio: Assets Selection.

Description:
    Crypto Currency Selection using monte Carlo simulation.
"""

# %% Import dependencies ----
# core
import os
import gc

# data science
import pandas as pd
import numpy as np
from scipy.stats import norm

# Cloud integration
from azureml.core import Workspace, Dataset, VERSION as aml_version
print(f'Azure ML SDK v{aml_version}')

# network
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# plots
import matplotlib.pyplot as plt
import seaborn as sns

# show info about python env
from IPython import sys_info
print(sys_info())

import warnings
warnings.filterwarnings("ignore")


# %% Set params ----
symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'MATICUSDT', 'UNIUSDT']

n_days = int(252) # US market has 252 trading days in a year
n_iterations = int(1e4)



# %% Load quotes ----
def get_quotes(symbol: str) -> pd.DataFrame:
    df = pd.read_csv(f'https://www.cryptodatadownload.com/cdd/Binance_{symbol}_d.csv', skiprows=[0])
    df = df.set_index('date')
    df = df.sort_values(by = 'date')

    return df[['symbol', 'open', 'high', 'low', 'close']]

quotes_data = [get_quotes(s) for s in symbols]
# row-wise union:
# pd.concat([get_quotes(s) for s in symbols])
# column-wise: 
# pd.concat(list1, axis=1, ignore_index=False)


btcusdt_df = quotes_data[0]

pd.concat([
    btcusdt_df['close'].head(5),
    btcusdt_df['close'].tail(5)
])



# %% Calculate Return
def get_returns(close_prices) -> pd.Series:
    return (close_prices/close_prices.shift()) - 1


btcusdt_df['diff'] = btcusdt_df['close'].diff()
btcusdt_df['return'] = get_returns(btcusdt_df['close'])

btcusdt_df[['close', 'diff', 'return']].tail(10)



# %% Calculate LogReturn
def get_log_returns(return_prices) -> pd.Series:
    return np.log(1 + return_prices)

btcusdt_df['log_return'] = btcusdt_df['return'].apply(lambda x: get_log_returns(x))
btcusdt_df[['close', 'diff', 'return', 'log_return']].tail(10)



# %% Simulate possible LogReturns

def get_simulated_returns(log_returns: pd.Series, n_days: int, n_iterations: int) -> pd.Series:
    u = log_returns.mean()
    var = log_returns.var()
    stdev = log_returns.std()

    drift = u - (0.5*var)
    Z = norm.ppf(np.random.rand(n_days, n_iterations))
    
    return np.exp(drift + stdev*Z)


btcusd_logreturns = btcusdt_df['log_return'].dropna()
btcusd_simulated_returns = get_simulated_returns(btcusd_logreturns, n_days, n_iterations)

assert(
    btcusd_simulated_returns.shape == (n_days, n_iterations)
)



# %% Monte carlo simulation functions ----
def get_breakeven_prob(predicted, threshold = 0):
    """
    This function calculated the probability of a stock being above a certain threshhold, which can be defined as a value (final stock price) or return rate (percentage change)
    """
    predicted0 = predicted.iloc[0,0]
    predicted = predicted.iloc[-1]
    predList = list(predicted)

    over = [(i*100)/predicted0 for i in predList if ((i-predicted0)*100)/predicted0 >= threshold]
    less = [(i*100)/predicted0 for i in predList if ((i-predicted0)*100)/predicted0 < threshold]

    return (len(over)/(len(over) + len(less)))


def monte_carlo_simulation(simulated_returns: pd.Series, last_actual_price: float, n_days: int, plot=True):
    # Create empty matrix
    price_list = np.zeros_like(simulated_returns)

    # Put the last actual price in the first row of matrix
    price_list[0] = last_actual_price

    # Calculate the price of each day
    for t in range(1, n_days):
        price_list[t] = price_list[t-1]*simulated_returns[t]
    
    # Plot
    if plot == True:
        x = pd.DataFrame(price_list).iloc[-1]
        fig, ax = plt.subplots(1, 2, figsize=(14,4))
        sns.distplot(x, ax=ax[0])
        sns.distplot(x, hist_kws={'cumulative': True}, kde_kws={'cumulative': True}, ax=ax[1])
        plt.xlabel('Stock Price')
        plt.show()
    

    print(f"Investment period: {n_days-1}")
    print(f"Expected Value: ${round(pd.DataFrame(price_list).iloc[-1].mean(),2)}")
    print(f"Return: {round(100*(pd.DataFrame(price_list).iloc[-1].mean()-price_list[0,1])/pd.DataFrame(price_list).iloc[-1].mean(),2)}%")
    print(f"Probability of Breakeven: {get_breakeven_prob(pd.DataFrame(price_list))}")
          
    return pd.DataFrame(price_list)


# %% Run Monte carlo simulation and estimate result

simulated_prices_df = monte_carlo_simulation(
    btcusd_simulated_returns, 
    quotes_data[0]['close'].tail(1), 
    n_days)


plt.figure(figsize=(10,6))
plt.plot(simulated_prices_df.iloc[:, 1:10])
plt.show()



# %% Monte Carlo simulation pipeline for multiple tokens ----

n_iterations = int(1e4) #! WARN: set simulations number

returns_data = [get_returns(df['close']) for df in quotes_data]
log_returns_data = [get_log_returns(r) for r in returns_data]
simulated_returns_data =  [get_simulated_returns(lr, n_days, n_iterations) for lr in log_returns_data]


for i in range(len(simulated_returns_data)):
    print(f'Starting Monte-Carlo simulation for {symbols[i]} symbol...')
    prices_ms = monte_carlo_simulation(simulated_returns_data[i], quotes_data[i]['close'].tail(1), n_days, plot=True)
    
    plt.figure(figsize=(10,6))
    plt.plot(prices_ms.iloc[:, 1:50])
    plt.show()

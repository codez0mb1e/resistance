#!/usr/bin/python3

"""
Data source: https://www.kaggle.com/datasets/tencars/392-crypto-currency-pairs-at-minute-resolution
"""

# %%
import os

import numpy as np
import pandas as pd
from sqlalchemy import types

from azure import AzureDbConnection, ConnectionSettings

# %%

# In terminal:
#> kaggle -v # must be >1.15
#> mkdir data; cd data
#> kaggle datasets download tencars/392-crypto-currency-pairs-at-minute-resolution
#> unzip 392-crypto-currency-pairs-at-minute-resolution.zip

input_dir = "../data"

# Get names and number of available currency pairs
pair_names = [x[:-4] for x in os.listdir(input_dir)]
usd_pairs = [s for s in pair_names if "usd" in s]

# Print the first 50 currency pair names
print(f"These are the first 10 out of {len(usd_pairs)} currency pairs in the dataset:")
print(usd_pairs[0:10])


# %%

def load_data(symbol: str, input_dir: str) -> pd.DataFrame:
    path_name = input_dir + "/" + symbol + ".csv"

    # Load data
    df = pd.read_csv(path_name, index_col='time', dtype={'open': np.float64, 'high': np.float64, 'low': np.float64, 'close': np.float64, 'volume': np.float64})
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df[~df.index.duplicated(keep='first')]

    # As mentioned in the description, bins without any change are not recorded.
    # We have to fill these gaps by filling them with the last value until a change occurs.
    #df = df.resample('1T').pad()

    return df[['open', 'high', 'low', 'close', 'volume']]


def calc_ohlcv_1h(df: pd.DataFrame) -> pd.DataFrame:
    df['hour'] = df.index.to_period('H')
    
    return (
        df
            .groupby(['hour'])
            .agg(
                {
                    'open': 'first',
                    'high': max,
                    'low': min,
                    'close': 'last',
                    'volume': sum,
                    #'time': max
                }
            )
            .reset_index()
        )


# %% ----
ethusd_1m = load_data("ethusd", input_dir)
ethusd_1h = calc_ohlcv_1h(ethusd_1m)

ethusd_1h.tail()



# %% ----
conn_settings = ConnectionSettings(
    'datainstinct',
    'market-data-db',
    'demo',
    '0test_test_AND_test'
)

db_conn = AzureDbConnection(conn_settings)
db_conn.connect()

for t in db_conn.get_tables():
    print(t)


# %%
db_mapping = {
    'FIGI': types.CHAR(length=12),
    'open': types.DECIMAL(precision=19, scale=9),
    'high': types.DECIMAL(precision=19, scale=9),
    'close': types.DECIMAL(precision=19, scale=9),
    'low': types.DECIMAL(precision=19, scale=9),
    'volume': types.DECIMAL(precision=19, scale=9),
    'time': types.DATETIME(),
    'source_id': types.SMALLINT(),
    'version': types.VARCHAR(length=12),
    'interval': types.CHAR(length=2)
}


# %%
pd.options.mode.chained_assignment = None 

min_candels_n = 10000

for pair in usd_pairs:
    print(f'INFO | {pair} > Starting read dataset...')

    candles_df = load_data(pair, input_dir)

    if len(candles_df) > min_candels_n:

        df = candles_df.loc['2022-07-01':'2022-10-01']

        if len(df) > 0:
            df = calc_ohlcv_1h(df)

            df['FIGI'] = pair
            df['time'] = df.hour.apply(lambda h: h.to_timestamp())
            df['source_id'] = 1
            df['version'] = 'v20221001'
            df['interval'] = '1H'
            df.drop(columns='hour', inplace=True)

            print(f'INFO | {pair} > Starting insert to DB...')
            print('DEBUG | {} rows from {} to {}'.format(df.shape[0], min(df['time']), max(df['time'])))
            db_conn.insert(df, 'crypto', db_mapping)
        else:
            print(f'WARN | {pair} > No new records')
    else:
        print(f'WARN | {pair} > Only {candles_df.shape[0]} records')


# %%
db_conn.dispose()

#!/usr/bin/python3

"""

Data source: https://www.kaggle.com/code/tencars/bitfinexdataset
"""

# %%
import os
import numpy as np
import pandas as pd
from sqlalchemy import types

from azure import AzureDbConnection, ConnectionSettings


# %%
input_path = "../data"

# Get names and number of available currency pairs
pair_names = [x[:-4] for x in os.listdir(input_path)]
n_pairs = len(pair_names)

# Print the first 50 currency pair names
print("These are the first 50 out of {} currency pairs in the dataset:".format(n_pairs))
print(pair_names[0:50])

usd_pairs = [s for s in pair_names if "usd" in s]
print(usd_pairs)

# %%

def load_data(symbol, source=input_path):
    path_name = source + "/" + symbol + ".csv"

    # Load data
    df = pd.read_csv(path_name, index_col='time', dtype={'open': np.float64, 'high': np.float64, 'low': np.float64, 'close': np.float64, 'volume': np.float64})
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df[~df.index.duplicated(keep='first')]

    # As mentioned in the description, bins without any change are not recorded.
    # We have to fill these gaps by filling them with the last value until a change occurs.
    #df = df.resample('1T').pad()

    return df[['open', 'high', 'low', 'close', 'volume']]


# %% ----
solusd = load_data("solusd")
solusd.tail()


# %% ----
conn_settings = ...
db_conn  = AzureDbConnection(conn_settings)

db_conn.connect()
for t in db_conn.get_tables():
    print(t)


# %%
min_candels_n = 10000

db_mapping = {
    'FIGI': types.VARCHAR(length=12),
    'open': types.DECIMAL(precision=19, scale=9),
    'high': types.DECIMAL(precision=19, scale=9),
    'close': types.DECIMAL(precision=19, scale=9),
    'low': types.DECIMAL(precision=19, scale=9),
    'volume': types.DECIMAL(precision=19, scale=9),
    'time': types.DATETIME(),
    'source_id': types.SMALLINT,
    'version': types.VARCHAR(length=12),
    'interval': types.CHAR(length=2)
}

for pair in usd_pairs:
    print(f'Starting read {pair}...')
    candles_df = load_data(pair)

    candles_df['FIGI'] = pair
    candles_df['time'] = candles_df.index
    candles_df['source_id'] = 128
    candles_df['version'] = 'v202204'
    candles_df['interval'] = '1M'

    if candles_df.shape[0] > min_candels_n:
        print('{} rows from {} to {}'.format(candles_df.shape[0], min(candles_df['time']), max(candles_df['time'])))

        print(f'Starting insert {pair}...')
        db_conn.insert(candles_df, 'Cryptocurrency', db_mapping)
    else:
        print(f'WARN: {pair} has only {candles_df.shape[0]} records')


# %%
db_conn.dispose()

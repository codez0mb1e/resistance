# %%
import numpy as np
import pandas as pd 
import time

from binance.client import Client


# %%
api_key = "****"
secret_key = "***"

client = Client(api_key, secret_key)


# %%
coins_response = client.get_all_coins_info()
coins_df = pd.DataFrame.from_dict(coins_response, orient='columns')


# %%
pairs_list = coins_df.coin.apply(lambda x: f"{x}USDT") 
client.get_historical_klines(
    'BTCUSDT', 
    interval=Client.KLINE_INTERVAL_1HOUR,
    start_str='2022-04-21', 
    end_str='2022-04-22'
)


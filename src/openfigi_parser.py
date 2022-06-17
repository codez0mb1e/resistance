# %%
import os
from dataclasses import dataclass
from typing import Literal, Union

import pandas as pd

import httpx

from sqlalchemy import types, sql
from azure import AzureDbConnection, ConnectionSettings


# %%
@dataclass
class AssetInfo:
    FIGI: str
    Ticker: str
    Title: Union[str, None]
    Description: Union[str, None]
    AssetType: Literal['Cryptocurrency']
    SourceId: Literal['OpenFigi API']
    Version: Literal['v202206']


def get_figi(pair: str) -> Union[AssetInfo, None]:
    """Return FIGI for pair

    References:
    - https://www.openfigi.com/assets/local/figi-allocation-rules.pdf
    - https://www.openfigi.com/search
    """
    api_url = f'https://www.openfigi.com/search/query?facetQuery=MARKET_SECTOR_DES:%22Curncy%22&num_rows=100&simpleSearchString={pair}&start=0'
    response = httpx.get(api_url)

    json_response = response.json()
    response_df = pd.DataFrame.from_dict(json_response['result'], orient='columns')
    if len(response_df) == 0:
        print(f'[WARN] {pair} not found')
        return None

    pair_figi = response_df.kkg_pairFIGI_sd.unique()

    if (len(pair_figi) != 1):
        print(f'[WARN] {len(pair_figi)} records was found for {pair}')
    else:
        print(f'[INFO] {pair} associated w/ FIGI {pair_figi[0]}')
    
    return pair_figi


# %% Tests
expected_pairs = {
    'WAX-USD': None,
    'ETH-USD': 'BBG00J3NBWD7',
    'BTC-USD': 'BBG006FCL7J4',
    'SOL-USD': 'BBG013WVY457',
    'UNI-USD': 'BBG013TZFVW3',
    'SUSHI-USD': 'KKG0000010W1'
}

for k, v in expected_pairs.items():
    actual = get_figi(k)
    print(actual)
    assert actual == v


# %%
pair_names = [x[:-4] for x in os.listdir("../data")]

def insert_dash(text: str, position: int) -> str:
    if '-' not in text:
        return text[:position] + '-' + text[position:]
    else:
        return text

usd_pairs = [
    insert_dash(s.upper(), 3)
    for s in pair_names if "usd" in s
]

print(usd_pairs)


pair_figi_list = [get_figi(p) for p in usd_pairs]

# %% ----
conn_settings = ConnectionSettings(server='***.database.windows.net', database='market-data-db', username='***', password='***')
db_conn = AzureDbConnection(conn_settings)

db_conn.connect()
for t in db_conn.get_tables():
    print(t)


# %%
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


query = sql.text("select * from Cryptocurrency where figi = 'ustusd'")
result = db_conn._conn.execute(query).fetchall()


# %%
db_conn.dispose()
print('Completed')

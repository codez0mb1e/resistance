
# %% Import dependencies
import os
from dataclasses import dataclass
from typing import Dict, Union

import pandas as pd

import httpx

from sqlalchemy import types
from azure import AzureDbConnection, ConnectionSettings


# %% Data models
@dataclass
class AssetInfo:
    FIGI: str
    Ticker: str
    Title: Union[str, None]
    Description: Union[str, None]
    AssetType: str = 'Cryptocurrency'
    SourceId: str = 'OpenFigi API'
    Version: str = 'v202206'

    def as_dict(self) -> Dict[str, str]:
        return {'Figi': self.FIGI, 'Ticker': self.Ticker}


# %% FIGI provider
class OpenFigiProvider:
    """
    OpenFigi API provider

    References:
            https://www.openfigi.com/assets/local/figi-allocation-rules.pdf
            https://www.openfigi.com/search
    """
    @staticmethod
    def _send_request(ticker: str, asset_type: str) -> pd.DataFrame:
        api_url = f'https://www.openfigi.com/search/query?facetQuery=MARKET_SECTOR_DES:%22{asset_type}%22&num_rows=100&simpleSearchString={ticker}&start=0'
        response = httpx.get(api_url)

        json_response = response.json()
        return pd.DataFrame.from_dict(json_response['result'], orient='columns')


    @staticmethod
    def _find_figi(df: pd.DataFrame, field_name: str) -> Union[str, None]:
        if len(df) == 0 or field_name not in df.columns:
            return None

        result = df[field_name].dropna().unique()
        
        if (len(result) != 1):
            print(f'[WARN] Multiple ({len(result)}) FIGI records was found')
            return None

        return result[0]


    @staticmethod
    def _find_name(df: pd.DataFrame) -> Union[str, None]:
        if len(df) == 0 or 'DS002_sd' not in df.columns:
            return None
            
         result = df['DS002_sd'].dropna().unique()
        
        if (len(result) != 1):
            print(f'[WARN] Multiple ({len(result)}) name records was found')
            return None

        return result[0]


    def search(self, ticker: str, asset_type: str = 'Curncy') -> Union[AssetInfo, None]:
        """Return FIGI for pair"""
        
        response_df = OpenFigiProvider._send_request(ticker, asset_type)

        figi = OpenFigiProvider._find_figi(response_df, 'kkg_pairFIGI_sd')

        if figi is None:
            base_quote = ticker.split('-')[0]
            print(f'[INFO] {ticker} > Try to search using base quote {base_quote}')

            response_df = OpenFigiProvider._send_request(base_quote, asset_type)
            figi = OpenFigiProvider._find_figi(response_df, 'kkg_baseAssetFigi_sd')

            if figi is None:
                return None

        return AssetInfo(figi, ticker, None, None)


#%%
figi_provider = OpenFigiProvider()

assert figi_provider.search('WAX-USD') == None
assert figi_provider.search('ABCD') == None


# %% Tests
expected_pairs = {
    'BNB-USD': 'KKG000007HZ5',
    'ETH-USD': 'BBG00J3NBWD7',
    'BTC-USD': 'BBG006FCL7J4',
    'SOL-USD': 'BBG013WVY457',
    'UNI-USD': 'BBG013TZFVW3',
    'SUSHI-USD': 'KKG0000010W1',
    'AVAX-USD': 'KKG000007J36'
}


for k, v in expected_pairs.items():
    actual = figi_provider.search(k)
    print(actual.as_dict())
    assert (
        isinstance(actual, AssetInfo)
        and actual.FIGI == v
        and actual.Ticker == k
    )


# %% Get assets for searching figi
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

print(usd_pairs[1:10])


# %%
figi_provider = OpenFigiProvider()
pair_figi_list = [figi_provider.search(p) for p in usd_pairs]


# %% ----
conn_settings = ConnectionSettings(server='****.database.windows.net', database='market-data-db', username='<user>', password='****')
db_conn = AzureDbConnection(conn_settings)

db_conn.connect()
for t in db_conn.get_tables():
    print(t)


# %%
db_mapping = {
    'Figi': types.CHAR(length=12),
    'Ticker': types.VARCHAR(length=12)
}

figi_df = pd.DataFrame([t.as_dict() for t in pair_figi_list if isinstance(t, AssetInfo)])
db_conn.insert(figi_df, 'figi', db_mapping)


# %%
db_conn.dispose()
print('Completed')

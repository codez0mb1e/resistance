# %%
from dataclasses import dataclass
from typing import Optional
import pandas as pd
import httpx


# %%
@dataclass
class AssetInfo:
    FIGI: str
    Ticker: str
    Title: str
    Description: Optional[str]
    AssetType: str = 'Cryptocurrency'
    SourceId: str = "OpenFigi API"
    Version: str = "v202204"


def get_asset_info(pair: str) -> AssetInfo:
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


#%% Tests
expected_pairs = {
    'WAX-USD': None,
    'ETH-USD': 'BBG00J3NBWD7',
    'BTC-USD': 'BBG006FCL7J4',
    'SOL-USD': 'BBG013WVY457',
    'UNI-USD': 'BBG013TZFVW3'
}

for k, v in expected_pairs.items():
    assert get_asset_info(k) == v


# %%
import os
import pandas as pd

pair_names = [x[:-4] for x in os.listdir("../data")]

def insert_dash(text: str, position: int) -> str:
    if '-' not in text:
        return text[:position] + '-' + text[position:]
    else:
        return text

usd_pairs = [insert_dash(s.upper(), 3) for s in pair_names if "usd" in s]

print(usd_pairs)

# %%
pair_figi_list = [get_asset_info(p) for p in usd_pairs]

for p in usd_pairs:
    print(p)
    get_asset_info(p)
# %%

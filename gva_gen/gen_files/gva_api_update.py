import numpy as np
import pandas as pd
import sys
from bs4 import BeautifulSoup as bs
import time
import requests
from requests_oauthlib import OAuth1
from pathlib import Path

def call_gva_data(page_range):
    print(page_range)
    print('starting call')

    # Call old Dataframe and make list
    file_path = Path(f'{sys.path[0]}/data_components/gva_all.csv')
    if file_path.is_file():
        gva_ex = pd.read_csv(file_path)
        print("Loading existing gva_all.csv")
        gva_inc = list(gva_ex['incident_id'].astype(str).str.rstrip('.0'))
        print(gva_inc[:10])
        gva_inc = [str(item) for item in gva_inc]
    else:
        gva_inc = []

    # Func to convert gva json to df type
    def gva_df_convert(json_df):
        wdf = pd.DataFrame(columns = list(json_df['results'][0].keys()))
        for index, row in json_df.iterrows():
            add_row = list(json_df['results'][index].values())
            wdf.loc[len(wdf)] = add_row
        return wdf

    # API ACCESS
    client_key = client_key
    client_secret= client_secret
    access_token = access_token
    token_secret = token_secret
    headers = headers
    headeroauth = OAuth1(client_key, client_secret,
                        access_token, token_secret,
                        signature_type='auth_header')
    
    complete_df = pd.DataFrame()
    for page in page_range:

        print('requesting page: '+str(page))
        protected_url = f'https://api.gunviolencearchive.org/api/incidents.json?page={page}&pagesize=500'
        r = requests.get(url=protected_url, headers=headers, auth=headeroauth)
        time.sleep(4)
        json_data = r.json()
        df = pd.DataFrame(json_data)
        fixed_df = gva_df_convert(df)
        print('merging page '+str(page)+' with all data')
        complete_df = pd.concat([complete_df, fixed_df], ignore_index=True)

        inc_lst = list(fixed_df['incident_id'])
        inc_lst = [str(item) for item in inc_lst]
        if any(id in inc_lst for id in gva_inc):
            print('Match found! Breaking the loop.')
            break
    print('merging new data to old dataframe')
    complete_df['incident_date'] = pd.to_datetime(complete_df['incident_date'])
    complete_df['year'] = complete_df['incident_date'].dt.year

    if file_path.is_file():
        complete_df = pd.concat([gva_ex, complete_df], ignore_index=True)
        print(complete_df.columns)
        print('dropping dupes')
        complete_df = complete_df[~complete_df['incident_id'].duplicated()]
        
    else:
        pass

    print(f'saving to: {str(file_path)}')
    complete_df.to_csv(f'{str(file_path)}', index=False)
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import time
import requests
from requests_oauthlib import OAuth1

save_path = '/Users/chall/Desktop/GitHub/CAP/Data/gva_all.csv'
page_range = [*range(0,1000)]

def call_gva_data(page_range, save_path):
    # Func to convert gva json to df type
    def gva_df_convert(json_df):
        wdf = pd.DataFrame(columns = list(json_df['results'][0].keys()))
        for index, row in json_df.iterrows():
            add_row = list(json_df['results'][index].values())
            wdf.loc[len(wdf)] = add_row
        return wdf

    # API ACCESS
    client_key = 'pCSMysBUwKVnHgmyrTXHCx52eomMxsaD'
    client_secret='mkXg9wSuWsVXpo96kccsJiN9vMByYcot'
    access_token = 'CXYEuJpu6eCYHNuzKYCCDsTWbiFia5q9'
    token_secret = 'uG6pxUsRoJo5BGqSkQJU2KmH76dRgcUL'
    headers = {'User-Agent':'Center for American Progress'}
    headeroauth = OAuth1(client_key, client_secret,
                        access_token, token_secret,
                        signature_type='auth_header')
    
    complete_df = pd.DataFrame()
    for page in page_range:

        print('requesting page: '+str(page))
        protected_url = f'https://api.gunviolencearchive.org/api/incidents.json?page={page}&pagesize=500&filters[IncidentDate][method]=isyear&filters[IncidentDate][field][date-year]=2022'
        r = requests.get(url=protected_url, headers=headers, auth=headeroauth)
        time.sleep(2)
        json_data = r.json()
        df = pd.DataFrame(json_data)
        fixed_df = gva_df_convert(df)
        print('merging page '+str(page)+' with all data')
        complete_df = pd.concat([complete_df, fixed_df], ignore_index=True)

    print('merging new data to old dataframe')
    complete_df['incident_date'] = pd.to_datetime(complete_df['incident_date'])
    complete_df['year'] = complete_df['incident_date'].dt.year
    # complete_df.rename(columns={'killed':'#_killed',
    #                         'injured':'#_injured',
    #                         'victims_killed': '#_victims_killed',
    #                         'victims_injured': '#_victims_injured',
    #                         'suspects_killed': '#_subjects-suspects_killed',
    #                         'suspects_injured':'#_subjects-suspects_injured'}, inplace=True)

    print('saving to: '+save_path)
    complete_df.to_csv(save_path, index=False)
    return complete_df




# save_path = '/Users/chall/Desktop/test.csv'
# page_range = [*range(0,20)]
# curr_df = call_gva_data(page_range=page_range, save_path=save_path)
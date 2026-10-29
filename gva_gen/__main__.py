import pandas as pd
import re
import os
import sys
from pathlib import Path
import numpy as np
from bs4 import BeautifulSoup as bs
import time
import requests
from requests_oauthlib import OAuth1

### add system path to get other library directories
current_dir = Path(__file__).resolve().parent
sys.path[0] = str(current_dir)

from gen_files.create_city_list import create_city_list
from gen_files.gva_api_update import call_gva_data
from gen_files.gva_df_gen_300_cities import cities_300_gen
from gen_files.filter_incidents import homs_only
from gen_files.merge_funcs import *
from gen_files.incident_handling import *
from gen_files.time_aggs import *
from gen_files.rolling_calc import rolling

### NEED PRIVATE API KEY AND ACCESS TOKEN FROM GVA TO RUN THIS SCRIPT ###

client_key = ''
client_secret=''
access_token = ''
token_secret = ''
headers = {'User-Agent':''}
headeroauth = OAuth1(client_key, client_secret,
                access_token, token_secret,
                signature_type='auth_header')

# Page range to check GVA
page_range = [*range(600,601)]
year = 2026

def main(current_dir, headers, headeroauth, page_range=page_range, final_year = year, agg = 'city', homs='true', time = 'annual'):

    ### Group_lst and Vars of Interest
    group_lst = ['city_state','city', 'state', 'year', 'pop']
    agg_dict = {'victims_killed': 'sum',
                'killed':'sum',
                'injured':'sum',
                'victims_injured': 'sum',
                'assault_weapon': 'sum',
                'ghost_gun':'sum',
                'domestic_violence': 'sum',
                'mass_shooting': 'sum',
                'hate_crime':'sum',
                'vic_child_killed':'sum',
                'vic_adult_killed':'sum',
                'vic_teen_killed':'sum',
                'vic_child_injured':'sum',
                'vic_adult_injured':'sum',
                'vic_teen_injured':'sum'}

    curr_df = call_gva_data(current_dir, headers, headeroauth, page_range)
    print('all called')

    city_list = create_city_list(current_dir)
# conditions
    if agg == 'city':
         print('agg to city')
         curr_df = cities_300_gen(curr_df, city_list, current_dir)
         print('filtered to 300 cities')
    else:
        pass

    if agg == 'state':
        standard_df = merge_state_pop(curr_df)
        standard_df['city'] = standard_df['city_or_county']
        print('agg\'d to states')
    else:
        standard_df = merge_city_pop(curr_df)

    if homs == 'true':
        standard_df = homs_only(standard_df)
        suffix = 'homs'
        print('filtered to homicides')
    else:
        print('converting incidents to lists')
        standard_df = incid_to_lst(standard_df)
        suffix = 'all'
        print('converted incidents to lists')

# incident handling
    print('making incident + participant dummies')
    standard_df = incid_dummy(standard_df, keys=['Assault weapon', 'Ghost gun', 'Domestic Violence','Mass Shooting', 'Hate Crime'])
    standard_df = partic_to_lst(standard_df)
    standard_df = partic_dummy(standard_df)
    print('saving dataframe to standard before time agg')

# Time aggregation level
    if time == 'annual':
        print('agg to annual')
        standard_df = annual_agg(standard_df, group_lst, agg_dict)
    elif time == 'month':
        print('agg to monthly')
        group_lst.append('month')
        standard_df = monthly_agg(standard_df, final_year, group_lst, agg_dict)
        # Calculate rolling averages
        print('add rolling')
        standard_df = rolling(standard_df)

# save to csv
    def suffix(time, homs, agg):
        if time == 'annual':
            t = 'annual'
        elif time == 'month':
            t = 'month'
        else:
            t = 'incident'
        if homs == 'true':
            h = 'homs'
        else:
            h = 'all'
        if agg == 'city':
            a = 'city'
        else:
            a = 'state'
        return f'{t}_{h}_{a}.csv'
    suffix = suffix(time, homs, agg)
    print('saving to csv')
    standard_df.to_csv(f'{str(current_dir)}/gva_gen/final_data/standard_df_{suffix}', index=False)

# Homicides Only, Annual, 300 City Filter
main(current_dir, headers, headeroauth, page_range,final_year = year, agg = 'city', homs= 'true', time='annual')

# Homicides Only, Monthly, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= 'true', time='month')

# All Incidents, Annual, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= '', time='annual')

# All Incidents, monthly, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= '', time='month')

# Homicides Only, States
main(group_lst, agg_dict, final_year = year, agg = 'state', homs= 'true', time='')

# All Incidents, States
main(group_lst, agg_dict, final_year = year, agg = 'state', homs= '', time='')

# Homicides Only, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= 'true', time='')

# All Incidents, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= '', time='')

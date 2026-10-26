import pandas as pd
import re
import os
import sys
from pathlib import Path
import numpy as np

# 1. Get the directory where the current script is located
current_dir = Path('__main__.py').resolve().parent

### add system path to get other library directories
sys.path[0] = os.path.join(os.path.abspath(''),'gva_gen/')

from create_city_list import city_list
from gva_api_update import call_gva_data
from gva_df_gen_300_cities import cities_300_gen
from filter_incidents import homs_only
from merge_funcs import *
from incident_handling import *
from time_aggs import *
from rolling_calc import rolling

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

# Save path and page range to check GVA
save_path = '/Users/chall/Desktop/GitHub/CAP/Data/gva_all.csv'
page_range = [*range(100,103)]
year = 2025

def main(group_lst, agg_dict, final_year = year, agg = 'city', homs='true', time = 'annual', final_save_path=''):

    curr_df = call_gva_data(page_range=page_range)
    print('all called')
# conditions
    if agg == 'city':
         print('agg to city')
         curr_df = cities_300_gen(curr_df, city_list)
         print('filtered to 300 cities')
    else:
        pass

    ############################################################
    ########## Toggled off adding grades and votign data ##########
    ############################################################

    # giff_df = pd.read_csv('/Users/chall/Desktop/GitHub/CAP/Data/gva_gen/data_components/giffords_score.csv')
    # voting_df = pd.read_csv('/Users/chall/Desktop/GitHub/CAP/Data/gva_gen/data_components/voting_data.csv')
    # states_complete = giffords_w_voting(giff_df, voting_df)
    # print('states_complete')
    # city_state_merged = gva_w_states(curr_df, states_complete)
    # print('city_state_merged')

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
    standard_df.to_csv(f'/Users/chall/Desktop/GitHub/CAP/Data/standard_300_{suffix}.csv')
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
    print('saving to csv')
    standard_df.to_csv(final_save_path, index=False)

# Homicides Only, Annual, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= 'true', time='annual', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/300_cities_hom_annual.csv')

# Homicides Only, Monthly, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= 'true', time='month', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/300_cities_hom_month.csv')

# All Incidents, Annual, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= '', time='annual', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/300_cities_all_annual.csv')

# All Incidents, monthly, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= '', time='month', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/300_cities_all_monthly.csv')

# Homicides Only, States
main(group_lst, agg_dict, final_year = year, agg = 'state', homs= 'true', time='', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/hom_all.csv')

# All Incidents, States
main(group_lst, agg_dict, final_year = year, agg = 'state', homs= '', time='', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/all_monthly.csv')

# Homicides Only, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= 'true', time='', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/300_cities_hom.csv')

# All Incidents, 300 City Filter
main(group_lst, agg_dict, final_year = year, agg = 'city', homs= '', time='', final_save_path = '/Users/chall/Desktop/GitHub/CAP/Data/Final Data Files/300_cities_all.csv')
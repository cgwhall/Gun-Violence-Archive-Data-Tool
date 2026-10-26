import pandas as pd
import re
import os
import sys
from pathlib import Path

current_dir = Path('merge_funcs.py').resolve().parent.parent
current_dir

def giffords_w_voting(giff_df, voting_df):
    giff_df.columns = giff_df.columns.str.lower()
    states_complete = pd.merge(voting_df, giff_df, on='state', how='outer')
    return states_complete
    

def gva_w_states(gva_df, states_complete):
    city_state_merged = pd.merge(gva_df, states_complete, on=['state', 'year'], how='left')
    return city_state_merged


def check_missing(df):
    df['pair'] = df['city'] + ', ' + df['state']
    included_cities = df['pair'].unique().tolist()
    missing = [item for item in city_list if item not in included_cities]
    if len(missing) > 0:
            print("Missing from dataset: " + missing)
    else:
        pass

def merge_city_pop(df):
    us_cities = pd.read_csv(f'{current_dir}/gva_gen/data_components/us-cities-table.csv')
    us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
    abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))
    us_cities['state'] = us_cities['usps'].map(abbrev_to_us_state)
    us_cities['city'] = us_cities['name']
    us_cities['city'] = us_cities['city'].str.replace('St.', 'Saint')
    us_cities['city'] = us_cities['city'].str.replace('New York City', 'New York')
    us_cities = us_cities.rename(columns={'pop2023':'pop'})
    us_cities = us_cities[['city','state','pop']]
    standard_df = pd.merge(df, us_cities, on=['city', 'state'], how='outer')
    return standard_df

def merge_state_pop(df):
    us_states = pd.read_csv(f'{current_dir}/gva_gen/data_components/state-population-table.csv')
    us_states = us_states.rename(columns={'pop2023':'pop'})
    us_states = us_states[['state','pop']]
    standard_df = pd.merge(df, us_states, on=['state'], how='outer')
    return standard_df
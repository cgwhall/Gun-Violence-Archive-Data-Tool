#######################################
## Using GVA All Data, Prepare 300 cities GVA database
#######################################

import numpy as np
import pandas as pd
import os
import sys
from pathlib import Path

def cities_300_gen(df, city_list, current_dir):

    # GVA has some weird or inconsistent name coventions; clean city names with mapping dictionary 
    city_mapping = {'Bronx': 'New York', 'Brooklyn': 'New York', 'Corona (Queens)': 'New York', 'Corona (queens)': 'New York', 'Queens':'New York', 'Arverne': 'New York', 'Staten Island':'New York', 'New York (Manhattan)': 'New York', 'East Los Angeles': 'Los Angeles', 'Spokane (Spokane Valley)': 'Spokane Valley', 'Mcallen': 'McAllen', 'Mcallen (McAllen)': 'McAllen', 'Salt Lake City (West Valley City)': 'West Valley City', 'Littleton (Lakewood)': 'Lakewood', 'Atlanta (Sandy Springs)': 'Sandy Springs', 'Hollywood (Miramar)': 'Miramar', 'Winston Salem (Winston-salem)': 'Winston-Salem', 'Winston Salem': 'Winston-Salem'}

    df['city_or_county'] = df['city_or_county'].replace(city_mapping)

    def replace_city_name(city):
        if city.startswith('Los Angeles'):
            return 'Los Angeles'
        else:
            return city
    df['city_or_county'] = df['city_or_county'].astype(str)
    df['city_or_county'] = df['city_or_county'].apply(replace_city_name)
    # filter down to only cities from city list
    df['filter'] = df['city_or_county'] + ', ' + df['state']
    df = df[df['filter'].isin(city_list)]

    # Check for any missing cities
    def check_missing(df):
        rem_cities = df['filter'].unique().tolist()
        len(rem_cities)
        missing = [str(item) for item in city_list if item not in rem_cities]
        if len(missing) > 0:
            print("Missing from GVA dataset: " + str(missing))
        else:
            pass
    check_missing(df)

    df.drop(columns='filter', inplace=True)

    cities_300_df = df.rename(columns={'city_or_county':'city','#_victims_killed':'gun_deaths', '#_victims_injured':'injured', '#_subjects-suspects_killed':'sus_killed','#_subjects-suspects_injured':'sus_inj', '#_subjects-suspects_arrested':'sus_arrested'})
    
    cities_300_df.to_csv(f'{current_dir}/gva_gen/data_components/gva_300_cities.csv', index=False)
    
    return cities_300_df
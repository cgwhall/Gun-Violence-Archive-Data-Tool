#libraries
import sys
import pandas as pd
from pathlib import Path


current_dir = Path('create_city_list.py').resolve().parent.parent

cities = pd.read_csv(f'{current_dir}/gva_gen/data_components/us-cities-table.csv')

# Fix city names to match GVA
cities['name'] = cities['name'].str.replace('St.', 'Saint')
cities['name'] = cities['name'].str.replace('New York City', 'New York')


# define dictionary to make conversion between abbreviations and state names
us_state_to_abbrev = {"Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA", "Colorado": "CO", "Connecticut": "CT","Delaware": "DE","Florida": "FL","Georgia": "GA","Hawaii": "HI","Idaho": "ID","Illinois": "IL","Indiana": "IN","Iowa": "IA","Kansas": "KS","Kentucky": "KY","Louisiana": "LA","Maine": "ME","Maryland": "MD","Massachusetts": "MA","Michigan": "MI","Minnesota": "MN","Mississippi": "MS","Missouri": "MO","Montana": "MT","Nebraska": "NE","Nevada": "NV","New Hampshire": "NH","New Jersey": "NJ","New Mexico": "NM","New York": "NY","North Carolina": "NC","North Dakota": "ND","Ohio": "OH","Oklahoma": "OK","Oregon": "OR","Pennsylvania": "PA","Rhode Island": "RI","South Carolina": "SC","South Dakota": "SD","Tennessee": "TN","Texas": "TX","Utah": "UT","Vermont": "VT","Virginia": "VA","Washington": "WA","West Virginia": "WV","Wisconsin": "WI","Wyoming": "WY","District of Columbia": "DC","American Samoa": "AS","Guam": "GU","Northern Mariana Islands": "MP","Puerto Rico": "PR","United States Minor Outlying Islands": "UM","U.S. Virgin Islands": "VI"}

#invert
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))

cities['usps'] = cities['usps'].replace(abbrev_to_us_state)

cities['city'] = cities['name']+ ', ' + cities['usps']
city_list = cities['city'].unique().tolist()
city_list.sort()
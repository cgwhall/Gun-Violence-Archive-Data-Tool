import pandas as pd
import re
import os
sys.path.insert(0,'/Users/chall/Desktop/GitHub/CAP/RedBlue/data_prep')
sys.path.insert(0,'/Users/chall/Desktop/GitHub/CAP/')
from create_city_list import city_list

city_list

### merge all into standard dataframe ###

# gva merge with mayors
cities_gva = pd.read_csv('RedBlue/Data/Components/gva_300_cities.csv')

# merge states with voting
states = pd.read_csv('RedBlue/Data/Components/state_laws_detailed.csv')
voting = pd.read_csv('RedBlue/Data/Components/voting_data.csv')


states_voting_merged = pd.merge(states, voting, on='state', how='inner')
states_voting_merged.to_csv('RedBlue/Data/Components/states_voting_merged.csv', index=False)


# merge states_voting_merged with giffords
states_voting_merged = pd.read_csv('RedBlue/Data/Components/states_voting_merged.csv')
giffords = pd.read_csv('RedBlue/Data/Components/giffords_score.csv')
giffords.columns = giffords.columns.str.lower()

states_complete = pd.merge(states_voting_merged, giffords, on='state', how='outer')
states_complete.to_csv('RedBlue/Data/Components/states_compl.csv', index=False)

# merge states_compl with gva
city_state_merged = pd.merge(cities_gva, states_complete, on=['state', 'year'], how='left')
city_state_merged.to_csv('RedBlue/Data/Components/gva_states.csv', index=False)


# ## Check for missing
# unique_pairs = city_state_merged[['city', 'state']].drop_duplicates()
# # Display the unique pairs
# print(unique_pairs)
# city_state_merged['pair'] = city_state_merged['city'] + ', ' + city_state_merged['state']
# included_cities = city_state_merged['pair'].unique().tolist()
# missing = [item for item in city_list if item not in included_cities]
# missing

#### FIX ACS CALL - MISSING CITIES
# # merge with acs to create standard df
# acs = pd.read_csv('RedBlue/Data/Components/cities_acs.csv')
# acs['city'] = acs['city'].str.replace('St.', 'Saint')
# temp_mapping = {'San Buenaventura (Ventura)':'Ventura',
#                 'Augusta-Richmond County consolidated government (balance)': 'Augusta',
#                 'Athens-Clarke County unified government (balance)': 'Athens'}
# acs['city'] = acs['city'].replace(temp_mapping)
# acs['state'] = acs['state'].str.strip()

# acs['pop']

# acs.columns
# acs = acs[acs['year'] == 2021]
# acs = acs[['state', 'city', 'pop']]

# Using world review instead
us_cities = pd.read_csv('RedBlue/Data/Components/us-cities-table.csv')

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
us_cities = us_cities.rename(columns={'pop':'pop2023'})

us_cities = us_cities[['city','state','pop']]

standard_df = pd.merge(city_state_merged, us_cities, on=['city', 'state'], how='outer')


# # Check for missing
unique_pairs = standard_df[['city', 'state']].drop_duplicates()
# Display the unique pairs
print(unique_pairs)
standard_df['pair'] = standard_df['city'] + ', ' + standard_df['state']
included_cities = standard_df['pair'].unique().tolist()
missing = [item for item in included_cities if item not in city_list]
missing

# Rearrange the columns
new_column_order = ['city'] + [col for col in standard_df.columns if col != 'city']
standard_df = standard_df[new_column_order]

# ### Bring in Wonder Data
# wonder = pd.read_csv('RedBlue/Data/Components/wonder_city_fltrd.csv')

# wonder = wonder.rename(columns={'State Name':'state',
#                                 'City Name':'city',
#                                 'Deaths':'deaths_cdc',
#                                 'Year':'year'})
# wonder['state'] = wonder['state'].str.title()
# # wonder
# # standard_df.columns
# standard_df = pd.merge(standard_df, wonder, on=['state', 'city', 'year'], how='left')



# SAVE TO STANDARD
standard_df.to_csv('RedBlue/Data/standard_df.csv', index=False)


#### STANDARD DF WITH ONLY HOMICIDES
standard_df = pd.read_csv('/Users/chall/Desktop/GitHub/CAP/RedBlue/Data/standard_df.csv')
standard_df = standard_df.dropna(subset=['incident_characteristics'])


# Convert incident_characteristics col to list object and clean values
def clean_incid_char(df):
    df['incident_characteristics'] = df['incident_characteristics'].str.replace(r'[\[\]\']', '', regex=True)
    df['incident_characteristics'] = df['incident_characteristics'].str.replace('(murder, accidental, suicide)', '',)
    df['incident_characteristics'] = df['incident_characteristics'].str.split(',').tolist()

    # CLEAN LIST OBJECT
    for index, row in df.iterrows():
        lst = df.loc[index, 'incident_characteristics']
        # print(index, lst)
        for lst_indx in range(len(lst)):
            clean_value = lst[lst_indx].strip()
            lst[lst_indx] = clean_value
        df.at[index, 'incident_characteristics'] = lst
    
    # ACCOUNT FOR MURDER/SUICIDE TAG
    for indx, row in df.iterrows():
        lst = df.loc[indx,'incident_characteristics']
        for lst_indx in range(len(lst)):
            if lst[lst_indx] == 'Murder/Suicide':
                for reloop_indx in range(len(lst)):
                    if lst[reloop_indx] == 'Suicide^':
                        del lst[reloop_indx]
                        break
                break
        df.at[indx, 'incident_characteristics'] = lst
    return df

standard_df = clean_incid_char(standard_df)

# # Test
standard_df.loc[1055, 'incident_characteristics']


# standard_df.columns.to_list()


## FILTERING STANDARD DF HOMICIDES ONLY
def filter_to(df):
    id_lst = []
    for index, row in df.iterrows():
        for item in df.loc[index,'incident_characteristics']:
            if 'Shot - Dead' in item:
                full_string = ' '.join(map(str, df.loc[index,'incident_characteristics']))
                if 'Suicide^' in full_string or 'Accidental Shooting' in full_string:
                    pass
                else:
                    id_lst.append(df.loc[index,'incident_id'])
                    break
    filt_df = df[df['incident_id'].isin(id_lst)]
    return filt_df

filtered_df = filter_to(standard_df)
filtered_df.columns

## Assign 2020_outcome of DC to be 'D'
filtered_df.loc[filtered_df['state'] == 'District of Columbia', '2020_outcome'] = 'D'

filtered_df.to_csv('RedBlue/Data/standard_df_homicides.csv')


## ACCIDENTAL ONLY
def filter_to_acc(df):
    id_lst = []
    for index, row in df.iterrows():
        for item in df.loc[index,'incident_characteristics']:
            if 'Shot - Dead' in item:
                full_string = ' '.join(map(str, df.loc[index,'incident_characteristics']))
                if 'Accidental Shooting' in full_string:
                    id_lst.append(df.loc[index,'incident_id'])
                    break
                else:
                    pass
    filt_df = df[df['incident_id'].isin(id_lst)]
    return filt_df

filtered_df = filter_to_acc(standard_df)
filtered_df = filtered_df.reset_index()
filtered_df
filtered_df.to_csv('RedBlue/Data/standard_df_acc.csv')


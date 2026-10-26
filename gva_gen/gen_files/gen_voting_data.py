# Generate Voting dataframe

import numpy as np
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs


### Add voting data
voting = pd.read_csv('RedBlue/Data/Components/dataverse_files/1976-2020-president.csv')

voting = voting[voting['year'] >= 2012]

states = pd.read('RedBlue/Data/Components/state_laws_detailed.csv')

state_list = states['abbr'].unique().tolist
years = [2012, 2016, 2020]

voting.columns

voting = voting[(voting['party_simplified'] == 'REPUBLICAN') | (voting['party_simplified'] == 'DEMOCRAT')]
voting['vote_share'] = voting['candidatevotes'] / voting['totalvotes']
voting = voting[['year', 'state', 'state_po', 'state_fips', 'candidatevotes', 'totalvotes', 'party_simplified', 'vote_share']]
voting_wide = voting.pivot_table(index=['year', 'state'], columns='party_simplified', values=['candidatevotes', 'totalvotes', 'vote_share'], aggfunc='first')
voting_wide = voting_wide.reset_index()
voting_wide.columns = voting_wide.columns.get_level_values(0) + '_' + voting_wide.columns.get_level_values(1)
voting_wide = voting_wide.reset_index()
voting_wide = voting_wide.drop(['index_','totalvotes_REPUBLICAN'], axis=1)
voting_wide.rename(columns={'year_':'year',
                            'state_':'state',
                            'totalvotes_DEMOCRAT':'totalvotes'}, inplace=True)
voting_wide.columns = voting_wide.columns.str.lower()
voting_wide['outcome'] = np.where(voting_wide['candidatevotes_democrat'] > voting_wide['candidatevotes_republican'], 1, 0)


voting_wider = voting_wide.pivot_table(index='state', columns='year', values=['vote_share_democrat', 'vote_share_republican', 'outcome'])
voting_wider.columns = [f'{col[1]}_{col[0]}' for col in voting_wider.columns]

voting_wider = voting_wider.reset_index()


years = [2012, 2016, 2020]
for year in years:
    voting_wider[f'{year}_outcome'] = np.where(voting_wider[f'{year}_outcome'] == 1, 'D', 'R')

# voting_wider.columns
voting_wider['state'] = voting_wider['state'].str.title()
voting_wider['state'] = voting_wider['state'].str.replace('Of', 'of')

voting_wider.to_csv('RedBlue/Data/Components/voting_data.csv', index=False)
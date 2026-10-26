
import pandas as pd
import re
import os
import sys
import numpy as np

## Read in all gva data
gva_all = pd.read_csv('/Users/chall/Desktop/GitHub/CAP/Data/gva_all.csv')

clean_gva = incid_to_lst(gva_all)

def mass_shooting_dummy(df):
    df['mass_shooting'] = 0
    id_lst = []
    for index, row in df.iterrows():
        lst = df.loc[index, 'incident_characteristics']
        if not isinstance(lst, list):
            pass
        else:
            for item in lst:
                if 'Mass Shooting' in item:
                    print('Mass Shooting at ', index)
                    df.at[index, 'mass_shooting'] = 1
                else:
                    pass
    return df

test = mass_shooting_dummy(clean_gva)

def incid_dummy(df, key=''):
    col_key = key.replace(' ', '_').lower()
    df[col_key] = 0
    id_lst = []
    for index, row in df.iterrows():
        lst = df.loc[index, 'incident_characteristics']
        if not isinstance(lst, list):
            pass
        else:
            for item in lst:
                if key in item:
                    #print(f'{key} at', index)
                    df.at[index, col_key] = 1
                else:
                    pass
    return df

test = incid_dummy(clean_gva, 'Defensive Use')


### Participant Handling
gva_all = pd.read_csv('/Users/chall/Desktop/GitHub/CAP/Data/gva_all.csv')
gva_all.columns
gva_all.head()
gva_all['participants'].head()

gva_all['participants'][0]
gva_all['participants'][0][0]

gva_test = gva_all.copy()
gva_test = gva_test[0:10000]

def extract_subset(string, start_symbol, end_symbol):
    start_index = string.find(start_symbol)
    end_index = string.find(end_symbol, start_index + len(start_symbol))  # Start search after start_symbol
    if start_index != -1 and end_index != -1:
        return string[start_index-1 + len(start_symbol):end_index+1]
    else:
        return None

gva_test['participants_lstd'] = [list() for x in range(len(gva_test.index))] #create empty col of lists
for index, row in gva_test.iterrows():
        participant_num = '{' # use parantheses to count participants in incident
        count = gva_test.loc[index, 'participants'].count(participant_num)
        print(index)
        for participant in range(count):
            sub_strg =  extract_subset(gva_test.loc[index, 'participants'], '{', '}')
            gva_test.loc[index, 'participants'] = gva_test.loc[index, 'participants'].replace(sub_strg, '')
            sub_strg = sub_strg.replace('{', '', ).replace('}', '', )
            sub_strg = sub_strg.replace('\'', '')
            sub_strg = sub_strg.replace(' ', '')
            sub_strg = sub_strg.split(',')
            gva_test.at[index, 'participants_lstd'].append(sub_strg)

gva_test['participants_lstd'][211][1]

sub_str = extract_subset(gva_test['participants'][0], '{', '}')
sub_str
sub_str = sub_str.replace('{', '', ).replace('}', '', )
sub_str = sub_str.replace('\'', '')
sub_str = sub_str.replace(' ', '')

def strip_itms(df):
    for index, row in df.iterrows():
        lst = df.loc[index, 'participants_lstd']
        #print(index, df.loc[index, 'incident_id'],  lst)
        count = 0
        if not isinstance(lst, list):
            count  += 1
            print(count)
            pass
        else:
            for lst_indx in range(len(lst)):
                clean_value = lst[lst_indx].strip()
                lst[lst_indx] = clean_value
        df.at[index, 'participants'] = lst
    return df


gva_test['participants_lstd'][211]


gva_all['participants_lstd'].head()


gva_test = gva_all.copy()

gva_test = gva_test[0:10000]


gva_test['participants_lstd'] = [list() for x in range(len(gva_all.index))]
sub_strg =  extract_subset(gva_test.loc[0, 'participants'], '{', '}').split(',')
gva_test.at[index, 'participants_lstd'].append(sub_strg)
gva_test.loc[index, 'participants'] = gva_test.loc[index, 'participants'].replace(sub_strg, '')


gva_test['participants_lstd'].head()


len(range(5))

x =0
for i in range(5):
    x += 1
    print(x)



################
################

sub_strg = extract_subset(gva_all['participants'][0], '{', '}')
print(sub_strg)

gva_all['participants'] = gva_all['participants'].str.replace(r'[\[\]\']', '', regex=True)
gva_all['participants'] = gva_all['participants'].str.replace(r'[\{\}\']', '', regex=True)
gva_all['participants'] = gva_all['participants'].str.replace('\'', '')
gva_all['participants'] = gva_all['participants'].str.split(',').tolist()

gva_all['participants'][0]
gva_all['participants'][0][2]

def strip_itms(df):
    for index, row in df.iterrows():
        lst = df.loc[index, 'participants']
        #print(index, df.loc[index, 'incident_id'],  lst)
        count = 0
        if not isinstance(lst, list):
            count  += 1
            print(count)
            pass
        else:
            for lst_indx in range(len(lst)):
                clean_value = lst[lst_indx].strip()
                lst[lst_indx] = clean_value
        df.at[index, 'participants'] = lst
    return df

gva_all = strip_itms(gva_all)

gva_all['participants'][0]

gva_all[gva_all['incident_id'] == 2765842]['participants']




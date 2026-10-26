import pandas as pd
import re
import os
import sys
import numpy as np

def incid_to_lst(df):
    def clean_incid_char(df):
        df = df.dropna(subset=['incident_characteristics'])
        df['incident_characteristics'] = df['incident_characteristics'].str.replace(r'[\[\]\']', '', regex=True)
        df['incident_characteristics'] = df['incident_characteristics'].str.replace('(murder, accidental, suicide)', '',)
        df['incident_characteristics'] = df['incident_characteristics'].str.split(',').tolist()
        return df
    def strip_itms(df):
        for index, row in df.iterrows():
            lst = df.loc[index, 'incident_characteristics']
            #print(index, df.loc[index, 'incident_id'],  lst)
            count = 0
            if not isinstance(lst, list):
                count  += 1
                pass
            else:
                for lst_indx in range(len(lst)):
                    clean_value = lst[lst_indx].strip()
                    lst[lst_indx] = clean_value
            df.at[index, 'incident_characteristics'] = lst
        return df
    df = clean_incid_char(df)
    df = strip_itms(df)
    
    print('filter suicides')
    for indx, row in df.iterrows():
        lst = df.loc[indx,'incident_characteristics']
        if not isinstance(lst, list):
            pass
        else:
            for lst_indx in range(len(lst)):
                if lst[lst_indx] == 'Murder/Suicide':
                    for reloop_indx in range(len(lst)):
                        if lst[reloop_indx] == 'Suicide^':
                            del lst[reloop_indx]
                            break
                    break
    df.at[indx, 'incident_characteristics'] = lst

    return df

def incid_dummy(df, keys=[]):
    for key in keys:
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

def partic_to_lst(df):
    df['participants_lstd'] = [list() for x in range(len(df.index))] #create empty col of lists
    for index, row in df.iterrows():
        if isinstance(df.loc[index, 'participants'], list):
            lst = df.loc[index, 'participants']
            lst = str(lst)
            df.at[index,'participants'] = lst
        else:
            pass
        split_list = df.loc[index, 'participants'].split('{')[1:]
        result_list = [item.split('}')[0] for item in split_list]
        df.at[index, 'participants_lstd'] = result_list
    return df


# Participant Group Dummies
def partic_dummy(df):
    df['vic_child_killed'] = 0
    df['vic_adult_killed'] = 0
    df['vic_teen_killed'] = 0
    df['vic_child_injured'] = 0
    df['vic_adult_injured'] = 0
    df['vic_teen_injured'] = 0
    for index, row in df.iterrows():
        ck_count = 0
        ak_count = 0
        tk_count = 0
        ci_count = 0
        ai_count = 0
        ti_count = 0
        for item in df.loc[index, 'participants_lstd']:
            if 'victim' in item and 'Teen 12-17' in item and 'Killed' in item:
                tk_count += 1
            if 'victim' in item and 'Child 0-11' in item and 'Killed' in item:
                ck_count += 1
            if 'victim' in item and 'Adult 18+' in item and 'Killed' in item:
                ak_count +=1
            if 'victim' in item and 'Teen 12-17' in item and 'Injured' in item:
                ti_count += 1
            if 'victim' in item and 'Child 0-11' in item and 'Injured' in item:
                ci_count += 1
            if 'victim' in item and 'Adult 18+' in item and 'Injured' in item:
                ai_count +=1
        df.at[index, 'vic_child_killed'] = ck_count
        df.at[index, 'vic_adult_killed'] = ak_count
        df.at[index, 'vic_teen_killed'] = tk_count
        df.at[index, 'vic_child_injured'] = ci_count
        df.at[index, 'vic_adult_injured'] = ai_count
        df.at[index, 'vic_teen_injured'] = ti_count
    return df






########################################## 
########################################## 
########################################## 
### DEPRECATED
### Participant Handling 
# def partic_to_lst(df):
#     def extract_subset(string, start_symbol, end_symbol):
#         start_index = string.find(start_symbol)
#         end_index = string.find(end_symbol, start_index + len(start_symbol))  # Start search after start_symbol
#         if start_index != -1 and end_index != -1:
#             return string[start_index-1 + len(start_symbol):end_index+1]
#         else:
#             return None

#     df['participants_lstd'] = [list() for x in range(len(df.index))] #create empty col of lists
#     for index, row in df.iterrows():
#         participant_num = '{' # use parantheses to count participants in incident
#         count = df.loc[index, 'participants'].count(participant_num)
#         print(index)
#         for participant in range(count):
#             sub_strg =  extract_subset(df.loc[index, 'participants'], '{', '}')
#             df.loc[index, 'participants'] = df.loc[index, 'participants'].replace(sub_strg, '')
#             sub_strg = sub_strg.replace('{', '', ).replace('}', '', )
#             sub_strg = sub_strg.replace('\'', '')
#             sub_strg = sub_strg.replace(' ', '')
#             sub_strg = sub_strg.split(',')
#             df.at[index, 'participants_lstd'].append(sub_strg)
#     return df






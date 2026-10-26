
#### STANDARD DF WITH ONLY HOMICIDES

import numpy as np

def homs_only(df):
    df = df.dropna(subset=['incident_characteristics'])
    def clean_incid_char(df):
        df['incident_characteristics'] = df['incident_characteristics'].str.replace(r'[\[\]\']', '', regex=True)
        df['incident_characteristics'] = df['incident_characteristics'].str.replace('(murder, accidental, suicide)', '',)
        df['incident_characteristics'] = df['incident_characteristics'].str.split(',').tolist()

        # CLEAN LIST OBJECT
        for index, row in df.iterrows():
            lst = df.loc[index, 'incident_characteristics']
            #print(index, df.loc[index, 'incident_id'],  lst)
            count = 0
            if not isinstance(lst, list):
                count  += 1
                #print(index)
                pass
            else:
                for lst_indx in range(len(lst)):
                    clean_value = lst[lst_indx].strip()
                    lst[lst_indx] = clean_value
            df.at[index, 'incident_characteristics'] = lst
        print(count)
        # ACCOUNT FOR MURDER/SUICIDE TAG
       # print('here')
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
    filt_df = clean_incid_char(df)

    ## FILTERING STANDARD DF HOMICIDES ONLY
    def filter_to(df):
        id_lst = []
        for index, row in df.iterrows():
            lst = df.loc[index, 'incident_characteristics']
            if not isinstance(lst, list):
                pass
            else:
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

    filt_df = filter_to(filt_df)

    return filt_df

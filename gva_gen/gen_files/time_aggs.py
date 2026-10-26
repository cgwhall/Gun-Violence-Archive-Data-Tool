import pandas as pd

def annual_agg(df, group_lst, var_dict):
    df['incident_date'] = pd.to_datetime(df['incident_date'])
    df['year'] = df['incident_date'].dt.year
    df['city_state'] = df['city']+', '+ df['state']
    for key in var_dict.keys():
        df[key] = df[key].astype(float)
    incid_df = df.groupby(group_lst)
    incid_df = incid_df.size()
    incid_df = incid_df.reset_index(name='incidents')
    df = df.groupby(group_lst).agg(var_dict).reset_index()
    merged_df = pd.merge(df, incid_df, on=group_lst, how='left')
    
    def pop_adj(df, var_dict):
        var_lst = list(var_dict.keys())
        for var in var_lst:
            df[f'{var}_pop_adj'] = (df[var] / df['pop'])*100000
        return df
    df = pop_adj(df, var_dict)
    return merged_df



def monthly_agg(df, final_year, group_lst, var_dict):
    df['incident_date'] = pd.to_datetime(df['incident_date'], format='mixed')
    df['year'] = df['incident_date'].dt.year
    df['month'] = df['incident_date'].dt.month
    df['city_state'] = df['city']+', '+ df['state']
    for key in var_dict.keys():
        df[key] = df[key].astype(float)
    incid_df = df.groupby(group_lst)
    incid_df = incid_df.size() # number of incidents
    incid_df = incid_df.reset_index()
    df = df.groupby(group_lst).agg(var_dict).reset_index()
    df = pd.merge(df, incid_df, on=group_lst, how='left')
    def no_incid_fix(df, final_year, var_dict):
        # Create params
        city_list = df['city_state'].unique().tolist()
        months_loop = list(range(1,13))
        year_loop = list(range(2014,final_year+1))

        col_lst = df.columns.to_list()
        month_indx = col_lst.index('month')
        year_indx = col_lst.index('year')
        #week_indx = col_lst.index('week')

        index_lst = []
        for key in var_dict.keys():
            index = col_lst.index(key)
            index_lst.append(index)

        for city in city_list:
            wdf = df.copy()
            wdf = wdf[wdf['city_state'] == city]
            #print(city)
            for year in year_loop:
                year_curr = wdf.copy()
                year_curr = year_curr[year_curr['year'] == year]
                months_included = year_curr['month'].unique().tolist()
                #print(year)
                for month in months_loop:
                    if month not in months_included:
                        if len(year_curr) != 0:
                            #print(month)
                            row = year_curr.iloc[0].tolist()
                            row[month_indx] = month
                            for i in index_lst:
                                row[i] = 0
                            df.loc[len(df)] = row
                            df.reset_index(drop=True, inplace=True)
                        if len(year_curr) == 0:
                            year_curr = wdf.copy()
                            year_curr = wdf[wdf['city_state'] == city]
                            #print(month)
                            row = year_curr.iloc[0].tolist()
                            row[year_indx] = year
                            row[month_indx] = month
                            for i in index_lst:
                                row[i] = 0
                            df.loc[len(df)] = row
                            df.reset_index(drop=True, inplace=True)
                    else:
                        pass
        return df
    df = no_incid_fix(df, final_year, var_dict)

    def pop_adj(df, var_dict):
        var_lst = list(var_dict.keys())
        for var in var_lst:
            df[f'{var}_pop_adj'] = (df[var] / df['pop'])*100000
        return df
    df = pop_adj(df, var_dict)
    return df
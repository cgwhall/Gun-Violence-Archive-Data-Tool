import pandas as pd

# Convert to Weekly
df = pd.read_csv('Data/standard_300_all.csv')

df.columns

# Test on Chicago
df = df[df['city'] == 'Chicago']
df = df[['incident_id', 'incident_date', 'state', 'city', 'killed', 'injured']]

df['incident_date'] = pd.to_datetime(df['incident_date'])
df['year'] = df['incident_date'].dt.year
df['month'] = df['incident_date'].dt.month
df['week'] = df['incident_date'].dt.isocalendar().week

# group by week
group_df = df.groupby(['city', 'state', 'year', 'month', 'week'])[['killed', 'injured']].sum()
group_df = group_df.reset_index()



group_df.to_csv('~/Desktop/week_test.csv', index = False)

def week_agg(df, group_lst, var_dict, final_year):
    df['incident_date'] = pd.to_datetime(df['incident_date'], format='mixed')
    df['year'] = df['incident_date'].dt.year
    df['week'] = df['incident_date'].dt.isocalendar().week
    df['city_state'] = df['city']+', '+ df['state']
    city_list = df['city_state'].unique().tolist()
    for key in var_dict.keys():
        df[key] = df[key].astype(float)
    def no_incid_fix(df, final_year, var_dict):
        # Create params
        city_list = df['city_state'].unique().tolist()
        weeks_loop = list(range(1,53))
        year_loop = list(range(2014,final_year+1))

        col_lst = df.columns.to_list()
        print(col_lst)
        week_indx = col_lst.index('week')
        year_indx = col_lst.index('year')

        index_lst = []
        for key in var_dict.keys():
            index = col_lst.index(key)
            index_lst.append(index)

        # progress counter
        tot = len(city_list)
        prog = 0
        for city in city_list:
            print(f'{prog} out of {tot} cities')
            wdf = df.copy()
            wdf = wdf[wdf['city_state'] == city]
            prog += 1


            for year in year_loop:
                year_curr = wdf.copy()
                year_curr = year_curr[year_curr['year'] == year]
                weeks_included = year_curr['week'].unique().tolist()
                #print(year)
                for week in weeks_loop:
                    if week not in weeks_included:
                        if len(year_curr) != 0:
                            #print(month)
                            row = year_curr.iloc[0].tolist()
                            row[week_indx] = week
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
                            row[week_indx] = week
                            for i in index_lst:
                                row[i] = 0
                            df.loc[len(df)] = row
                            df.reset_index(drop=True, inplace=True)
                    else:
                        pass
        return df
    df = no_incid_fix(df, final_year, var_dict)
    print('here')

    df = df.groupby(['city_state', 'city', 'state', 'year', 'week', 'pop']).agg(var_dict).reset_index()        

    def pop_adj(df, var_dict):
        var_lst = list(var_dict.keys())
        for var in var_lst:
            df[f'{var}_pop_adj'] = (df[var] / df['pop'])*100000
        return df
    df = pop_adj(df, var_dict)
    return df

group_lst = ['city_state','city', 'state', 'year', 'pop']
agg_dict = {'victims_killed': 'sum',
            'killed':'sum',
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


df = pd.read_csv('Data/Final Data Files/300_cities_hom.csv')
week_df = week_agg(df, group_lst, agg_dict, final_year=2024)

week_df.to_csv('~/Desktop/week_test.csv', index = False)
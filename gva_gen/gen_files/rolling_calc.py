import pandas as pd

def rolling(df, var_lst = ['victims_killed', 'victims_injured']):
    for var in var_lst:
        rolling_avg = df.groupby('city_state')[var].rolling(window=12, min_periods = 12).mean().reset_index(drop=True)
        df[f'{var}_roll'] = rolling_avg
    return df

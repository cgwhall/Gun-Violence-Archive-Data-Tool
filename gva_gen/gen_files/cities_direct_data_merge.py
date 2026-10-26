import numpy as np
import pandas as pd
import os
import zipfile
import requests
from bs4 import BeautifulSoup as bs

city_data_path = '/Users/chall/Desktop/GitHub/CAP/RedBlue/Data/City Gun Violence/City Data'

if os.path.exists('RedBlue/Data/City Gun Violence/City Data/Calls_for_Service_2022_NOLA.csv'):
    pass
else:
    for file_name in os.listdir(city_data_path):
        file_path = os.path.join(city_data_path, file_name)

        # Check if the file is a zip file
        if zipfile.is_zipfile(file_path):
            # Extract the contents of the zip file to the same folder
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(city_data_path)




###### BALTIMORE
baltimore = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Baltimore/Baltimore_Crime_Data.csv')

baltimore['Weapon'].unique()
balt_weapons = ['FIREARM','HANDGUN','SHOTGUN','OTHER_FIREARM', 'AUTOMATIC_HANDGUN', 'RIFLE', 'AUTOMATIC_FIREARM', 'AUTOMATIC_RIFLE']
baltimore = baltimore[baltimore['Weapon'].isin(balt_weapons)]

baltimore.columns
baltimore

baltimore['Description'].unique()
baltimore = baltimore[['CrimeDateTime', 'CrimeCode', 'Description', 'Weapon', 'Total_Incidents']]
baltimore['Description'].unique()
baltimore['CrimeDateTime'] = pd.to_datetime(baltimore['CrimeDateTime'])
baltimore['year'] = baltimore['CrimeDateTime'].dt.year
baltimore = baltimore[(baltimore['year'] >= 2015) & (baltimore['CrimeDateTime'] < '2023-06-01')]
balt_23 = baltimore[(baltimore['CrimeDateTime'] > '2022-12-31') & (baltimore['CrimeDateTime'] <= '2023-04-22')]
# balt_23_shootings = balt_23[balt_23['Description'] == 'SHOOTING']
# balt_23_homicides = balt_23[balt_23['Description'] == 'HOMICIDE']
# balt_23_homicides
# balt_23_shootings

years = baltimore['year'].unique().tolist()
years

other_crimes = ['ROBBERY', 'AGG. ASSAULT', 'LARCENY', 'ROBBERY - CARJACKING', 'ROBBERY - COMMERCIAL', 'COMMON ASSAULT', 'AUTO THEFT', 'RAPE', 'BURGLARY', 'LARCENY FROM AUTO', 'ARSON']
balt_df = pd.DataFrame({'year':[],
                        'shootings':[],
                        'homicides':[],
                        'incidents_other':[]})

def agg_balt(balt_df, years, incidents, city=''):
    agg_df = pd.DataFrame({'year':[],
                        'shootings':[],
                        'homicides':[],
                        'incidents_other':[]})

    for year in years:
        wdf = balt_df.copy()
        wdf = wdf[wdf['year'] == year]
        shootings = len(wdf[wdf['Description'] == 'SHOOTING'])
        homs = len(wdf[wdf['Description'] == 'HOMICIDE'])
        incidents_other = len(wdf[wdf['Description'].isin(incidents)])
        new_row = [year, shootings, homs, incidents_other]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = 'Baltimore'
    return agg_df

balt_df = agg_balt(baltimore, years, other_crimes, city='Baltimore')
balt_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/baltimore.csv')


###### SEATTLE

seattle = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Seattle/Shootings & Shots Fired by Yr.csv')
seattle = seattle.melt(id_vars=['Shooting Type Group'], value_vars=['2015', '2016','2017','2018', '2019', '2020', '2021', '2022', '2023'])

seattle = pd.pivot(seattle,index='variable', columns=['Shooting Type Group'], values='value').reset_index()
seattle = seattle.rename(columns={'variable':'year'})

###### BOSTON
boston = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Boston/Boston_shootings.csv')
col = 'shooting_date'
year_filter = [2015,'2023-05-01']

def year_select(df,date_column, time_params):
    df[date_column] = pd.to_datetime(df[date_column])
    df['year'] = df[date_column].dt.year 
    df = df[(df['year'] >= time_params[0]) & (df[date_column] <= time_params[1])]
    return df

boston = year_select(boston, col, year_filter)


def agg_boston(df, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'shootings':[],
                        'homicides':[]})

    for year in years:
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]
        shootings = len(wdf[wdf['shooting_type_v2'] == 'Non-Fatal'])
        homs = len(wdf[wdf['shooting_type_v2'] == 'Fatal'])
        new_row = [year, shootings, homs]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

bos_df = agg_boston(boston, 'Boston')
bos_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/boston.csv')


########  NEW ORLEANS
paths = {2023:'j3gz-62a2',
         2022:'9wdb-bznc',
         2021:'6pqh-bfxa',
         2020:'hjbe-qzaz',
         2019:'mm32-zkg7',
         2018:'3m97-9vtw',
         2017:'qtcu-97s9',
         2016:'4gc2-25he',
         2015:'9ctg-u58a'}


nola = pd.read_csv('https://data.nola.gov/resource/9wdb-bznc.csv?$limit=50000&$offset=50000')

signals = nola['signal_description'].unique().tolist()

gun_signals = [signal for signal in signals if 'SHOOTING' in signal or 'FIREARM' in signal or 'GUN' in signal]

shootings = ['AGGRAVATED BATTERY (SHOOTING)', 'ARMED ROBBERY (GUN)', 'ATTEMPTED ARMED ROBBERY (GUN)', 'ATTEMPTED MURDER (SHOOTING)']
homs = ['HOMICIDE (SHOOTING)']
other = ['ILLEGAL CARRYING OF A GUN']

def agg_nola(paths, shootings, homs, other, col ='', city=''):
    agg_df = pd.DataFrame({'year':[],
                        'shootings_nonf':[],
                        'homicides':[],
                        'incidents_other':[]})

    for path in paths:
        wdf1 = pd.read_csv(f'https://data.nola.gov/resource/{paths[path]}.csv?$limit=50000&$offset=0')
        wdf2 = pd.read_csv(f'https://data.nola.gov/resource/{paths[path]}.csv?$limit=50000&$offset=50000')
        wdf = pd.concat([wdf1, wdf2])
        shootings_agg = len(wdf[wdf[col].isin(shootings)])
        homs_agg = len(wdf[wdf[col].isin(homs)])
        incidents_agg = len(wdf[wdf[col].isin(other)])
        new_row = [path, shootings_agg, homs_agg, incidents_agg]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

nola = agg_nola(paths, shootings, homs, other, col ='signal_description', city='New Orleans')
nola
nola.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/nola.csv')


###### Chicago
chicago = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Chicago/Chicago_Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings.csv')
chicago.columns

col = 'DATE'
chicago = year_select(chicago,col, year_filter)
chicago = chicago[chicago['GUNSHOT_INJURY_I'] == 'YES']

description = chicago['INCIDENT_PRIMARY'].unique().tolist()
description = ['BATTERY', 'ROBBERY', 'NON-FATAL'] # after removing homicides

def agg_city_simple(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'shootings':[],
                        'homicides':[]})

    for year in years:
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]
        shootings = len(wdf[wdf[col].isin(description)])
        homs = len(wdf[wdf[col] == 'HOMICIDE'])
        new_row = [year, shootings, homs]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

chi_df = agg_city_simple(chicago,col='INCIDENT_PRIMARY',city= 'Chicago')
chi_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/chicago.csv')


####### MINNEAPOLIS ############
min = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Minneapolis/Crime_Data_MIN.csv')
min2 = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Minneapolis/Crime_Data.csv')

col = 'Occurred_Date'
min = year_select(min,col, year_filter)
min2 = year_select(min2,col, year_filter)
min2 = min2[min2['year'] < 2019]
min = pd.concat([min, min2])
min['year'].unique()

min['Problem_Final'].unique() # 'Shooting (PFE)', 'Sound of Shots Fired (P)', 'Shooting Report Only (P)'

shooting_reports = ['Shooting (PFE)', 'Sound of Shots Fired (P)', 'Shooting Report Only (P)']
min = min[min['Problem_Final'].isin(shooting_reports)]

min['Offense_Category'].unique()
shootings_other = ['Assault Offenses ', 'Subset of NIBRS Assault Offenses',
       'Weapon Law Violations ',
       'Subset of NIBRS Robbery',
       'Destruction/Damage/Vandalism of Property ',
       'Burglary/Breaking & Entering ', 'Robbery ',
       'Drug/Narcotic Offenses ', 'Fraud Offenses ',
       'Stolen Property Offenses ', 'Motor Vehicle Theft ',
       'Larceny/Theft Offenses ', 'Animal Cruelty ',
       'Kidnapping/Abduction ', 'Arson ', 'Sex Offenses ',
       'Counterfeiting/Forgery ',
       'Shots Fired Calls']

min['year'].unique()
def agg_city_simple(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'shootings_inj':[],
                        'shootings_other':[],
                        'homicides':[]})

    for year in years:
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]
        shootings_other_agg= len(wdf[wdf[col].isin(shootings_other)])
        shootings_inj_agg = len(wdf[wdf[col] == 'Gunshot Wound Victims'])
        homs = len(wdf[wdf[col] == 'Homicide Offenses '])
        new_row = [year, shootings_inj_agg,shootings_other_agg, homs]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

min_df = agg_city_simple(min,col='Offense_Category',city= 'Minneapolis')
min_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/minneapolis.csv')


######## Cincinati #############
cinci = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Cinci/PDI__Police_Data_Initiative__CPD_Shootings_CINCI.csv')

col = 'DATETIME'
cinci = year_select(cinci,col, year_filter)

def agg_city_simple(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'shootings':[],
                        'homicides':[]})

    for year in years:
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]
        shootings_inj_agg = len(wdf[wdf[col] == 'NONFATAL'])
        homs = len(wdf[wdf[col] == 'FATAL'])
        new_row = [year, shootings_inj_agg, homs]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

cinci_df = agg_city_simple(cinci,col='TYPE',city= 'Cincinati')
cinci_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/cincinati.csv')


########### Durham #############
durham1 = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Durham/dpd_incidents_(ucr_nibrs_reporting)_Durham.csv')

durham1['Weapon'].unique()
list_weapons = ['Handgun','Rifle','Undetermined Firearm','Shotgun','Other Firearm']

durham1 = durham1[durham1['Weapon'].isin(list_weapons)]

col = 'Report Date'
durham1 = year_select(durham1,col, year_filter)

durham1['Offense'].unique()
offense_lst = ['AGGRAVATED ASSAULT', 'VANDALISM', 'WEAPON VIOLATIONS',
       'ROBBERY - INDIVIDUAL', 'ROBBERY - COMMERCIAL', 'BURGLARY',
       'DRUG EQUIPMENT/PARAPHERNALIA', 'STOLEN PROPERTY',
       'KIDNAPPING/ABDUCTION', 'SEX OFFENSE - FORCIBLE RAPE',
       'ALL OTHER OFFENSES-CITY ORDINANCE VIOLATIONS',
       'DRUG/NARCOTIC VIOLATIONS', 'CALLS FOR SERVICE (NO CRIME)',
       'LARCENY - FROM BUILDING', 'ALL OTHER CRIMINAL OFFENSES',
       'ROBBERY - BANK', 'DRIVING WHILE IMPAIRED',
       'ALL TRAFFIC (EXCEPT DWI)', 'SUICIDE',
       'ALL OTHER OFFENSES-PAROLE/PROBATION VIOLATIONS', 'INTIMIDATION',
       'FOUND PROPERTY', 'ASSIST OTHER AGENCY',
       'DV INFO REPORT (NO CRIME)',
       'NON-CRIMINAL DETAINMENT (INVOLUNTARY COMMITMENT)',
       'SEX OFFENSE - FORCIBLE SODOMY', 'MOTOR VEHICLE THEFT',
       'RECOVERED STOLEN PROPERTY (OTHER JURISDICTION)',
       'LARCENY - FROM MOTOR VEHICLE', 'LOST PROPERTY',
       'HOMICIDE - NEGLIGENT MANSLAUGHTER', 'DISORDERLY CONDUCT',
       'CRIME SCENE INVESTIGATION', 'ALL OTHER OFFENSES-COURT VIOLATIONS',
       'ALL OTHER OFFENSES-ESCAPE FROM CUSTODY OR RESIST ARREST',
       'SUSPICIOUS ACTIVITY', 'LARCENY - ALL OTHER',
       'DEATH INVESTIGATION', 'OFFENSES AGAINST FAMILY - CHILD ABUSE',
       'RECOVERED STOLEN VEHICLE (OTHER JURISDICTION)',
       'FRAUD-IDENTITY THEFT', 'ARSON',
       'DISORDERLY CONDUCT-FIGHTING (AFFRAY)', 'SEX OFFENSE - FONDLING',
       'LARCENY - SHOPLIFTING', 'TRESPASSING', 'RUNAWAY',
       'ANIMAL CRUELTY', 'SEX OFFENSE - SEXUAL ASSAULT WITH AN OBJECT',
       'OFFENSES AGAINST FAMILY - NEGLECT', 'TOWED/ABANDONED VEHICLE',
       'MISSING PERSON', 'FRAUD - FALSE PRETENSE',
       'DISORDERLY CONDUCT-DRUNK AND DISRUPTIVE']

col = 'Offense'
def agg_city_simple(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'gun_related_crimes':[],
                        'homicides':[]})

    for year in years:
    
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]

        shootings_agg = len(wdf[wdf[col].isin(offense_lst)])
        homs_agg = len(wdf[wdf[col].str.contains('HOMICIDE')])
        new_row = [year, shootings_agg, homs_agg]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

durham_df = agg_city_simple(durham1, col, city='Durham')
durham_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/durham.csv')


########### Fort Worth #############
fortw = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Fort Worth/fort_worth.csv')

fortw = fortw[fortw['Description'].str.contains('Deadly Weapon F')]
fortw['Nature Of Call'].unique()


lst = []
for index, row in enumerate(fortw['Description']):
    if 'Deadly Weapon F' in fortw.loc[index]['Description']:
        lst.append(row)

lst


########### Hartford #############
hartford = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Hartford/Hartford_Police_Incidents_01012005_to_05182021.csv')

keywords = ['GUN', 'SHOOTING', 'SHOT', 'FIREARM']
hartford = hartford[hartford['UCR_1_Description'].str.contains('|'.join(keywords))]
hartford['UCR_1_Description'].unique()

col = 'Date'
hartford = year_select(hartford,col, year_filter)

shooting_codes = ['SHOTS FIRED - UNCONFIRMED', 'SURRENDERED FIREARM',
       'SHOTS FIRED - CONFIRMED', 'ILL CARRY FIREARM-UI', 'ASSLT-1-GUN',
       'ASSLT-2-GUN', 'MURDER-HANDGUN', 'ROBBERY-GUN *COMMER*',
       'ROBBERY-GUN *STREET*', 'SHOTS SPOTTER', 'DISCHARGE GUN',
       'RECOVERED STOLEN FIREARM', 'ROBBERY-GUN *GAS ST*',
       'ROBBERY-GUN *RESID*',
       'POSS FIREARM IN/ON SCH PR', 'GUN BUYBACK', 'PD-SHOOTING',
       'STOLEN FIREARM', 'ROBBERY-GUN *ALL OTHER', 'ROBBERY-GUN *TAXI*',
       'ASSLT-PO-GUN', 'GUN-ATT-SUIC', 'SHOOTING-INJ', 'MURDER-SHOTGUN',
       'DRIVE BY SHOOTING', 'ROBBERY-GUN *BANK*', 'ASSLT-EMT-GUN',
       'FIREARMS-ACC', 'SHOOTING-MISS']

col = 'UCR_1_Category'
def agg_city_simple(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'shootings':[],
                        'homicides':[]})

    for year in years:
    
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]

        shootings_agg = len(wdf[(wdf['UCR_1_Description'].isin(shooting_codes)) & (wdf['UCR_2_Category'] == '52* - SHOTS FIRED')])
        homs_agg = len(wdf[wdf[col].str.contains('HOMICIDE')])
        new_row = [year, shootings_agg, homs_agg]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

hartford_df = agg_city_simple(hartford, col, 'Hartford')
hartford_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/hartford.csv')

########### Jacksonville #########


########### Mesa #############




########### New York #############
ny_df = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/New York/NYPD_Shooting_Incident_Data__Historic_.csv')

ny_df['OCCUR_DATE'] = pd.to_datetime(ny_df['OCCUR_DATE'])
ny_df['year'] = ny_df['OCCUR_DATE'].dt.year

def agg_city_simple(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'shootings':[],
                        'homicides':[]})

    for year in years:
    
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]

        shootings_agg = len(wdf['INCIDENT_KEY'].unique())
        homs_agg = len(wdf[wdf[col] == True])
        new_row = [year, shootings_agg, homs_agg]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

ny_agg = agg_city_simple(ny_df, 'STATISTICAL_MURDER_FLAG', 'New York')
ny_agg.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/newyork.csv')


########### Los Angeles #############
la_df = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Los Angeles/Crime_Data_from_2020_to_Present (1).csv')

la_df.columns

crimes = la_df['Crm Cd Desc'].unique().tolist()
crimes.sort()
crimes

la_df['Date Rptd'] = pd.to_datetime(la_df['Date Rptd'])
la_df['year'] = la_df['Date Rptd'].dt.year

la_df['Weapon Desc'].unique().tolist()

la_df[la_df['Crm Cd Desc'] == 'DISCHARGE FIREARMS/SHOTS FIRED']

def agg_city_la(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'gun_incid':[],
                        'homicides':[]})
    firearm_lst = ['SEMI-AUTOMATIC PISTOL', 'HAND GUN', 'SHOTGUN','UNKNOWN FIREARM',  'OTHER FIREARM',
                   'AIR PISTOL/REVOLVER/RIFLE/BB GUN', 'REVOLVER', 'RIFLE', 'ASSAULT WEAPON/UZI/AK47/ETC', 'ANTIQUE FIREARM', 'SEMI-AUTOMATIC RIFLE',
                   'MAC-11 SEMIAUTOMATIC ASSAULT WEAPON','HECKLER & KOCH 93 SEMIAUTOMATIC ASSAULT RIFLE', 'SAWED OFF RIFLE/SHOTGUN',
                   'AUTOMATIC WEAPON/SUB-MACHINE GUN', 'M1-1 SEMIAUTOMATIC ASSAULT RIFLE', 'STARTER PISTOL/REVOLVER', 'MAC-10 SEMIAUTOMATIC ASSAULT WEAPON',
                   'RELIC FIREARM', 'HECKLER & KOCH 91 SEMIAUTOMATIC ASSAULT RIFLE', 'UZI SEMIAUTOMATIC ASSAULT RIFLE', 'UNK TYPE SEMIAUTOMATIC ASSAULT RIFLE', 'M-14 SEMIAUTOMATIC ASSAULT RIFLE']
    df = df[df['Weapon Desc'].isin(firearm_lst)]

    for year in years:
    
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]

        gun_incid = len(wdf)
        homs_agg = len(wdf[wdf[col] == 'CRIMINAL HOMICIDE'])
        new_row = [year, gun_incid, homs_agg]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

la_agg = agg_city_la(la_df, 'Crm Cd Desc', 'Los Angeles')
la_agg

la_agg.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/losangeles.csv')

la_df_2019 = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Los Angeles/Crime_Data_from_2010_to_2019 (2).csv')
la_df_2019['Date Rptd'] = pd.to_datetime(la_df_2019['Date Rptd'])
la_df_2019['year'] = la_df_2019['Date Rptd'].dt.year
la_agg_2019 = agg_city_la(la_df_2019, 'Crm Cd Desc', 'Los Angeles')
la_agg_2019 = la_agg_2019[la_agg_2019['year'] < 2020]
la_agg_2019


########### Dallas #############
dal_df = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Dallas/Police_Incidents.csv')

dal_df.columns

dal_df['Weapon Used'].unique().tolist()
firearms = ['Handgun', 'Other Firearm', 'Firearm (Type Not Stated)', 'Rifle', 'Other Gun', 'Shotgun', 'Assault Weapon']

dal_df = dal_df[(dal_df['Year of Incident'] > 2015) & (dal_df['Weapon Used'].isin(firearms))]

dal_df.to_csv('RedBlue/Data/City Gun Violence/City Data/Dallas/Police_Incidents_reduced.csv')

incids = dal_df['Type of Incident'].unique().tolist()
incids.sort()
incids

hom = ['HOMICIDE', 'MURDER']

def agg_city_simple(df, col, city=''):
    years = df['Year of Incident'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'gun_incid':[],
                        'homicides':[]})

    for year in years:
    
        wdf = df.copy()
        wdf = wdf[wdf['Year of Incident'] == year]

        shootings_agg = len(wdf)
        homs_agg = len(wdf[wdf[col] == 'HOMICIDE OFFENSES'])
        new_row = [year, shootings_agg, homs_agg]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

dal_agg = agg_city_simple(dal_df, 'NIBRS Crime Category', 'Dallas')

dal_agg

homs_2022 = dal_df[(dal_df['Year of Incident'] == 2022) & (dal_df['NIBRS Crime Category'] == 'HOMICIDE OFFENSES')]  
len(homs_2022)

dal_df = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Dallas/2020_homicides.csv')


########### Nashville #############
nash_df = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Nashville/Metro_Nashville_Police_Department_Incidents.csv')
nash_df['Incident Occurred'] = pd.to_datetime(nash_df['Incident Occurred'])
nash_df['year'] = nash_df['Incident Occurred'].dt.year


offenses = nash_df['Offense Description'].unique().tolist()
offenses.sort()
offenses

firearms  = nash_df['Weapon Description'].unique().tolist()
firearms = ['HANDGUN', 'HANDGUN - SEMIAUTOMATIC','OTHER FIREARM','REVOLVER', 'RIFLE', 'SHOTGUN']
nash_df = nash_df[nash_df['Weapon Description'].isin(firearms)]

hom = ['HOMICIDE', 'HOMICIDE, JUSTIFIABLE', 'HOMICIDE- CRIMINAL', 'HOMICIDE- CRIMINALLY NEGLIGENT']

def agg_city_simple(df, col, city=''):
    years = df['year'].unique().tolist()
    agg_df = pd.DataFrame({'year':[],
                        'homicides':[]})

    for year in years:
    
        wdf = df.copy()
        wdf = wdf[wdf['year'] == year]

        homs_agg = len(wdf[wdf[col].isin(hom)])
        new_row = [year, homs_agg]
        agg_df.loc[len(agg_df)] = new_row
    agg_df['city'] = city
    return agg_df

nash_agg = agg_city_simple(nash_df, 'Offense Description', 'Nashville')

nash_agg.to_csv('RedBlue/Data/City Gun Violence/City Data/Agg Data/nashville.csv')


########### Philadelphia #############
phil_df = pd.read_csv('RedBlue/Data/City Gun Violence/City Data/Philadelphia/shootings_PHI.csv')

hom_2022 = phil_df[(phil_df['year'] == 2022) & (phil_df['fatal'] == 1)]
len(hom_2022)

hom_2021 = phil_df[(phil_df['year'] == 2021) & (phil_df['fatal'] == 1)]

len(hom_2021)
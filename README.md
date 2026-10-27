# Gun Violence Archive (GVA) Data Pull & Tool
### Chandler Hall
**Last updated October 2026

# About
This repository pulls and cleans data directly from the Gun Violence Archive using a private API, and merges gun violence incident data with community-level social and economic indicators. Use this repository to pull gun violence incident data into analysis-ready datasets, with arguments to aggregate by:

- **Geography:** state or city
- **Time period:** week, month, or year
- **Homicides only:** filters incidents and 'killed' count to account for suicides and accidental shootings

By default, datasets relate observations with data from the American Community Survey and state grades of gun laws provided by the Giffords Law Center. Final datasets also add features to raw GVA incident data based on participant and event characteristics. See Data Dictionary below and under Data Subfolder.

This project is not affiliated with the Gun Violence Archives, and the repository requires a private API key and access codes to run locally (email mark@gvadata.org to request). Download most recently updated end-product data files [here](https://drive.google.com/drive/folders/1BEIW6A1CKqRTDy4Anj0LAglaA3yJJ0SE?usp=sharing).

# Quickstart
Use [__main__.py](https://github.com/cgwhall/Gun-Violence-Archive-Data-Tool/blob/main/gva_gen/__main__.py) to under [gva_gen](https://github.com/cgwhall/Gun-Violence-Archive-Data-Tool/tree/main/gva_gen) subfolder to make data call.

** **You will need to enter API and access token information before running.** Email mark@gvadata.org to request

# Data Dictionary

In addition to the incident features in the raw GVA data, this tool adds:

| Feature | Type | Description |
| :--- | :---: | ---: |
| assault_weapon | numeric | 1 if assault weapon reported in incident, 0 otherwise |
| ghost_gun | numeric | 1 if ghost gun reported in incident, 0 otherwise |
| domestic_violence | numeric | 1 if reported as domestic violence, 0 otherwise |
| mass_shooting | numeric | 1 if 4 or more victims injured/killed, 0 otherwise |
| hate_crime | numeric | 1 if ghost gun reported in incident, 0 otherwise |
| vic_child_killed | numeric | total count of killed victims aged <12|
| vic_adult_killed | numeric | total count of killed victims aged 18+ |
| vic_teen_killed | numeric | total count of killed victims aged 12-1 |
| vic_child_injured | numeric | total count of injured victims aged <12 |
| vic_adult_injured | numeric | total count of injured victims aged 18+ |
| vic_teen_injured | numeric | total count of injured victims aged 12-17 |

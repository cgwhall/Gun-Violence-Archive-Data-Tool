# Gun Violence Archive (GVA) Data Pull & Tool
### Chandler Hall

**Last updated October 2026

# About
This repository pulls and cleans data directly from the Gun Violence Archive through the use of private API, and merges gun violence incident data with community-level social and economic indicators. Use this repository to pull gun violence incident data into analysis-ready datasets, with arguments to aggregate by:

- **Geography:** state or city
- **Time period:** week, month, or year
- **Homicides only:** filters incidents and 'killed' count to account for suicides and accidental shootings

By default, datasets relate observations with data from the American Community Survey and state grades of gun laws provided by the Giffords Law Center. Final datasets also add features to raw GVA incident data based on participant and event characteristics, including:

- assault weapon used
- ghost gun used
- domestic violence incident
- mass shooting incident
- hate crime incident
- victim age cohort
  - child (age XX - XX)
  - teen (age XX - XX)
  - adult (age XX+) 

This project is not affiliated with the Gun Violence Archives and the repository requires a private API key and access codes to run locally (email mark@gvadata.org to request). For most recently updated end-product data files, download directly from:

# Table of Contents
- main
- gva_gen
  - data components
  - gva_files

# Quickstart
--

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:33:11 2023

@author: chandlerhall
"""

import requests
from bs4 import BeautifulSoup as bs

year_range = [*range(2015,2023)]

def scrape_giffords(year_range, current_year):
    def scrape_one(url, year):
        response = requests.get(url)
        soup = bs(response.content, "html.parser")
        tbody = soup.find_all('tbody')
        rows = []
        for tr in tbody[0].find_all("tr"):
            row = [td.text.strip() for td in tr.find_all("td")]
            row.insert(3, str(year))
            rows.append(row[1:4])
        return rows
    
    def scrape_head(url):
        response = requests.get(url)
        soup = bs(response.content, "html.parser")
        header = soup.find('thead')
        tr = header.find("tr")
        head = [th.text.strip() for th in tr.find_all("th")]
        head = [item.replace(' ','') for item in head]
        head = [item.replace('\n','') for item in head]
        head.insert(3, 'year')
        head=head[1:4]
        return head

    url = 'https://giffords.org/lawcenter/resources/scorecard/'
    rows = scrape_one(url, current_year)
    head = scrape_head(url)
    rows.insert(0, head)

    for year in year_range:
        if year == 2015 or year ==2016:
            url = f'https://giffords.org/scorecard{year}/'
            new_year = scrape_one(url, year)
            for row in new_year:
                rows.append(row)
        else:
            url = f'https://giffords.org/lawcenter/resources/scorecard{year}/'
            new_year = scrape_one(url, year)
            for row in new_year:
                rows.append(row)
    return rows

giffords = scrape_giffords(year_range, current_year=2023)

def save_to_csv(data, path):
    # Join and save to github folder
    lines = [','.join(line) for line in data]
    doc = '\n'.join(lines)
    with open(path, 'w') as ofile:
        ofile.write(doc)
        
save_to_csv(giffords, '/Users/chall/Desktop/GitHub/CAP/Data/gva_gen/data_components/giffords_score.csv')
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:10:39 2022

@author: Hp
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("transformed_data.csv")
data2 = pd.read_csv("raw_data.csv")
print(data)

print(data.head())
print(data2.head())

# Checking out how many sample of each country is present in our dataset

data['COUNTRY'].value_counts(sort=True, ascending=False)

# checking out the mode, mean and median values
print(data['COUNTRY'].value_counts().mode())
print(data['COUNTRY'].value_counts().mean())
print(data['COUNTRY'].value_counts().median())


"""So 294 is the mode value, using it for dividing the sum of all the samples
related to the human development index, GDP per capita, and the population."""
# creating a new dataset by combining the necessary columns from both datasets

#Aggregating the data

code = data['CODE'].unique().tolist()
country = data['COUNTRY'].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data['pop'].unique().tolist()
gdp = []

for i in country:
    hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)
    tc.append((data2.loc[data['location'] == i, 'total_cases']).sum())
    td.append((data2.loc[data2['location'] == i, 'total_deaths']).sum())
    sti.append((data.loc[data['COUNTRY'] == i, 'STI']).sum()/294)
    population.append((data2.loc[data2['location'] == i, 'population']).sum()/294)
    
aggregated_data = pd.DataFrame(list(zip(code, hdi, tc, td, population)), 
                                   columns = ['Country Code', 'Country', 'HDI', 
                                              'Total Cases', 'Total Deaths', 
                                              'Stringency Index', 'Population'])
    
print(aggregated_data.head())

#Sorting Data according to total cases

data = aggregated_data.sort_values(by=["Total Cases"], ascending = False)
print(data.head())
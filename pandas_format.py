# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 08:03:40 2021

@author: monic
"""

# Pandas es el formato para variables y observaciones

# puede trabajar con diferentes tipos de variables, se construye sobre NumPy

#%%

dict = { "country":["Brazil", "Russia", "India", "China", "South Africa"],
        "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
        "area":[8.516, 17.10, 3.286, 9.597, 1.221],
        "population":[200.4, 143.5, 1252, 1357, 52.98] }

#%%
import pandas as pd
brics = pd.DataFrame(dict)

print(brics)

#%%
brics.index = ["BR", "RU", "IN", "CH", "SA"]

print(brics)

#%%
# importing from csv

brics = pd.read_csv('./examples-datacamp/brics.csv')
print(brics)

brics = pd.read_csv("./examples-datacamp/brics.csv", index_col = 0)
print(brics)

#%%
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictiona: ry my_dict with three key:value pairs: my_dict
my_dict = {"names": names, "dr": dr, "cpc": cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

#%%
# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars.index = row_labels

# Si seleccionamos con [ ] nos genera un tipo especial de array unidimensional. Si queremos un dataframe usamos [[]]

print(brics["country"])
print(type(brics["country"]))


print(brics[["country"]])
print(type(brics[["country"]]))

# Access to rows

print(brics[1:4])

# rows and columns

print(brics.loc["RU"])

print(brics.loc[["RU"]])

print(brics.loc[["RU", "IN"]])

print(brics.loc[["RU", "IN"]], ["country", "capital"])


print(brics.loc[:, ["country", "capital"]])

# rows and columns by position

print(brics.iloc[:, [0,1]])

# %%

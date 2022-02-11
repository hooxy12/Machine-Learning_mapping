# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 19:18:09 2022

@author: HP
"""
###
#using the str.lower series method map between houses rent
#and their prices per your hometown rental prices. 

import pandas as pd

#creating types of rental houses
housesRent = ['Condo','Townhouse','Apartment','Bangalow','Cabin']

#creating mapping data
prices_to_houses={'townhouse':350,'bangalow':800,'condo':230,'apartment':150
                  ,'cabin':100}

#Create DataFrame
data = pd.DataFrame({'houses_rent': housesRent})

#since the prices_to_houses is lowercase, 
# hense the the data is converted to lowercase
data_new = data['houses_rent'].str.lower()

#Mapping
data['prices per month']=data_new.map(prices_to_houses)

#data with new column 'prices per month" is created
data


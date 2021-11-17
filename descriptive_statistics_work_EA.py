#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:35:28 2021

@author: elise140

From https://www.kaggle.com/hamelg/python-for-data-21-descriptive-statistics
by Greg Hamel

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read companylist.csv
companylist = pd.read_csv("companylist.csv")
#only needed if there are extra spaces in the column names
#companylist.columns = companylist.columns.str.strip() 

#print companylist to ensure that the file is correct
companylist
#print some column names to see that they work
companylist.Name
companylist.MarketCap
companylist.columns.values

#calculate the mean of each column
#this works for the last sale and IPO year
#but the Market cap has $, M, and N in addition to numbers
companylist.mean()

#get the median for numerical columns
companylist.median()

#get the mode for numerical columns
companylist.mode()

#calculate the variance
companylist.var()

#calculate the standard deviation
companylist.std()

#skewness
companylist.skew()

#kurtosis
companylist.kurt()

#calculate range (not working because of missing values?)
#pd.options.mode.use_inf_as_na = True
max(companylist["LastSale"]) - min(companylist["LastSale"])

#quartiles written out
five_num = [companylist["LastSale"].quantile(0),
            companylist["LastSale"].quantile(0.25),
            companylist["LastSale"].quantile(0.50), 
            companylist["LastSale"].quantile(0.75),
            companylist["LastSale"].quantile(1)]
five_num

#quartiles using describe
companylist["LastSale"].describe()

#interquartile range
companylist["LastSale"].quantile(0.75) - companylist["LastSale"].quantile(0.25)

#boxplot
#check plots tab
#formatting isn't great!
companylist.boxplot(column="LastSale",
                    return_type="axes",
                    figsize=(8,8))

plt.text(x=0.74, y=22.25, s="3rd Quartile")
plt.text(x=0.8, y=18.75, s="Median")
plt.text(x=0.75, y=15.5, s="1st Quartile")
plt.text(x=0.9, y=10, s="Max")
plt.text(x=0.7, y=19.5, s="IQR", rotation=90, size=25)
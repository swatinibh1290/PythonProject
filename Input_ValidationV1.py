# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:14:58 2021

@author: Hari
"""
import datetime
import pandas as pd
file_location = "D:\Learning\Semester 1\Intro to Python Programming\Assignment\company_list.csv"
col_list = ["Symbol", "Name","Last Sale"]
df = pd.read_csv(file_location, usecols=col_list)
#view the first five rows: 
print(df)

def input_period():
    flag = False
    while(flag != True):
        period = input("Please enter the period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max): ")
        if(period == "1d" or period == "5d" or period=="1mo" or period == "3mo" or period=="6mo" or period == "1y" or period=="2y" or period == "5y" or period=="10y" or period == "ytd" or period=="max"):
            flag = True
        else:
            print("Invalid period")
    return period

def input_date(time_frame):
    flag = False
    while(flag != True):
        date = input("Please choose "+ time_frame +" date in (YYYY-MM-DD): ")
        try:
            flag = bool(datetime.datetime.strptime(date, '%Y-%m-%d'))
        except ValueError:
            flag = False
            print("Invalid " + time_frame +" date")
    return date
            
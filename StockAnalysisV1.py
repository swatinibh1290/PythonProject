# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:33:32 2021

@author: Hari
"""

import yfinance as yf
import pandas as pd
import numpy as np
from Input_ValidationV1 import input_period, input_date
from ticker_plot import export_data, get_ticker_data, get_company_details
from GraphAnalysisV1 import raw_time, simple_moving, cumulative_moving, exponential_moving, macd
import seaborn as sb
import matplotlib.pyplot as plt


def get_company_list():
    file_location = "D:\Learning\Semester 1\Intro to Python Programming\Assignment\company_list.csv"
    col_list = ["Symbol", "Name","Last Sale","% Change"]
    df = pd.read_csv(file_location, usecols=col_list)
    return df

def t_and_c():
    """Display terms and conditions from 'terms.txt'"""
    for line in open("terms.txt"):
        print(line, end = "")

def display_welcome():
    print('Welcome to the Stock Quote Application -- Access real-time data on stocks\n')

def display_menu():
    print("Services Offered:")
    print("1. Search Stocks\n2. Query Time Range\n3. Export Data\n4. Graphical displays\n98. Read T&C\n99. Quit")



def get_choice():
    return input("Please choose option : ")

def search_stocks(company_list):
    print('Search Stocks')
    print(company_list)
    #data = None
    #while data is None:
    symbol = input("Please choose ticker symbol: ")
    filtered_companies = company_list[(company_list.Symbol.str.lower().str.contains(symbol.lower())) | (company_list.Name.str.lower().str.contains(symbol.lower()))]
    if(filtered_companies.shape[0] == 1):  
        print(filtered_companies)
    elif(filtered_companies.shape[0] >= 2):
        print(filtered_companies)
        symbol=input("Please select the exact ticker symbol: ")
        get_company_details(symbol)
    else:
        print("Else statement")
        get_company_details(symbol)
    stock_history=input("Would you like to know the stock history? (Yes/No):")
    if(stock_history.lower()=="yes"):
        period = input_period()
        get_ticker_data(symbol,period)


def get_stock_history():
    print('Query Time Range')
    data = None
    while data is None:
        try:
            symbol = input("Please choose ticker symbol: ")
            period = input_period()
            data = get_ticker_data(symbol, period)
            print("-----------------------------------------------")
            print(data)
        except KeyError:
            print('Invalid Symbol - Please try again.')

def download_data():
    print('Export Data')
    data = None
    while data is None:
        try:
            symbol = input("Please choose ticker symbol: ")
            start = input_date("start")
            end = input_date("end")
            data = export_data(symbol, start, end)
        except KeyError:
            print('Invalid Symbol - Please try again.')
    
def process_choice(choice, company_list):
    while choice != "99":
        if choice == "1":
            search_stocks(company_list)
        elif choice == "2":
            get_stock_history()
        elif choice == "3":
            download_data()
        elif choice == "4":
            all_graphs()
        elif choice == "98":
            t_and_c()
        else:
            print("Wrong choice, please try again.")
        display_menu()
        choice = get_choice()
def graph_choice_menu():
    print("What descriptive statistics would you like to view?")
    print("1. Raw time series\n2. Simple moving average\n3. Exponential moving average\n4. Cumulative moving average\n5. MACD\n6. Quit")

def get_choice():
    return input("Please choose option: ")

def graph_choice(choice1,symbol,period,start,end):
    while choice1 != "6":
        if choice1 == "1":
            raw_time(symbol,period,start,end)
        elif choice1 == "2":
            simple_moving(symbol,period,start,end)
        elif choice1 == "3":
            exponential_moving(symbol,period,start,end)
        elif choice1 == "4":
            cumulative_moving(symbol,period,start,end)
        elif choice1 =="5":
            macd(symbol,period,start,end)
        else:
            print("Wrong choice, please try again.")
        graph_choice_menu()
        choice1 = get_choice()

def all_graphs():
    symbol = input("Please choose ticker symbol: ")
    period = input_period()
    start = input_date("start")
    end = input_date("end")
    graph_choice_menu()
    choice1 =get_choice()
    graph_choice(choice1,symbol,period,start,end)
    
def main():
    company_list = get_company_list()
    # Create a menu for the stock quotes app
    display_welcome()
    display_menu()
    # ask the user for their choice
    choice = get_choice()
    # process the choice
    process_choice(choice, company_list)
    

if __name__ == '__main__':
    main()
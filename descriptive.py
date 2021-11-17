# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:39:59 2021

@author: surya
"""

import yfinance as yf
import pandas as pd
import numpy as np
from ticker_plot import export_data, get_ticker_data
from graph import raw_time, simple_moving, cumulative_moving, exponential_moving, macd
import seaborn as sb
import matplotlib.pyplot as plt


def get_company_list():
    return pd.read_csv('companylist.csv')

def t_and_c():
    """Display terms and conditions from 'terms.txt'"""
    for line in open("terms.txt"):
        print(line, end = "")

def display_welcome():
    print('Welcome to the Stock Quote Application')

def display_menu():
    print("1. Search Stocks\n2. Query Time Range\n3. Export Data\n4. Graphical dispalys\n98. Read T&C\n99. Quit")



def get_choice():
    return input("Please choose option: ")

def search_stocks(company_list):
    print('Search Stocks')
    symbol = input("Please choose ticker symbol: ")
    filtered_companies = company_list[
        (company_list.Symbol.str.lower().str.contains(symbol.lower()))
                | (company_list.Name.str.lower().str.contains(symbol.lower()))]
    print(filtered_companies)
    print(filtered_companies.describe())

def get_stock_history():
    print('Query Time Range')
    data = None
    while data is None:
        try:
            symbol = input("Please choose ticker symbol: ")
            period = input("Please choose period: (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)")
            data = get_ticker_data(symbol, period)
        except KeyError:
            print('Invalid Symbol - Please try again.')

def download_data():
    print('Export Data')
    data = None
    while data is None:
        try:
            symbol = input("Please choose ticker symbol: ")
            start = input("Please choose start period: (YYYY-MM-DD)")
            end = input("Please choose end period: (YYYY-MM-DD)")
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

def graph_choice(choice4):
    while choice4 != "6":
        if choice4 == "1":
            raw_time()
        elif choice4 == "2":
            simple_moving()
        elif choice4 == "3":
            exponential_moving()
        elif choice4 == "4":
            cumulative_moving()
        elif choice4 =="5":
            macd()
        else:
            print("Wrong choice, please try again.")
        graph_choice_menu()
        choice4 = get_choice()

def all_graphs():
    graph_choice_menu()
    choice4=get_choice()
    graph_choice(choice4)
    
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:43:24 2020

@author: dredmond

Your task is to write a computer program,
which allows users to consult/analyse/model stock times-series.
It will source its data online,
but should optimise the use of downloaded data,
to avoid excessive network traffic.

Assume your users are advanced Business Analysts,
but without programming knowledge.
They should have the possibility of searching for specific stocks,
and query specified time ranges,
along with associated analysis,
such as statistical descriptions of prices and/or volume
(mean, median, range, etc), technical indicators,
visualisation (of the raw data, but also of transformations,
such as moving averages),
and even basic modelling (such as regression).

The program should provide a comprehensive but easy to use
and intuitive interface (text or graphical).

"""

import pandas as pd
from ticker_plot import export_data, get_ticker_data

def get_company_list():
    return pd.read_csv('companylist.csv')

def t_and_c():
    """Display terms and conditions from 'terms.txt'"""
    for line in open("terms.txt"):
        print(line, end = "")

def display_welcome():
    print('Welcome to the Stock Quote Application')

def display_menu():
    print("1. Search Stocks\n2. Query Time Range\n3. Export Data\n98. Read T&C\n99. Quit")
    
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
        elif choice == "98":
            t_and_c()
        else:
            print("Wrong choice, please try again.")
        display_menu()
        choice = get_choice()

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

    

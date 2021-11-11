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

def t_and_c():
    """Display terms and conditions from 'terms.txt'"""
    for line in open("terms.txt"):
        print(line, end = "")

def display_welcome():
    print('Welcome to the Stock Quote Application')

def display_menu():
    print("1. Search Stocks\n2. Query Time Range\n3. Read T&C\n4. Quit")
    
def get_choice():
    return input("Please choose option: ")

def process_choice(choice):
    while choice != "4":
        if choice == "1":
            print('Search Stocks')
        elif choice == "2":
            print('Query Time Range')
        elif choice == "3":
            t_and_c()
        else:
            print("Wrong choice, please try again.")
        choice = get_choice()

def main():
    # Create a menu for the stock quotes app
    display_welcome()
    display_menu()
    # ask the user for their choice
    choice = get_choice()
    # process the choice
    process_choice(choice)

if __name__ == '__main__':
    main()

    

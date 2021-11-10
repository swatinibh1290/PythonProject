"""
Created on Sun Nov 9, 9:45 2021

@author: Emma Matthews

Your task is to write a computer program, 
which allows users to consult/analyse/model stock times-series.
It will source its data online, but should optimise the use of downloaded data,
to avoid excessive networktraffic.

Assume your users are advanced Business Analysts,
but without programming knowledge. Theyshould have the possibility of 
searching for specific stocks, and query specified time ranges, 
along withassociated analysis, such as statistical descriptions of prices and/or volume
(mean, median, range, etc),technical indicators, 
visualisation (of the raw data, but also of transformations, such as moving averages),
and even basic modelling (such as regression).

The program should provide a comprehensive but easy to use and intuitive interface.

"""
import ystockquote 


def t_and_c():
    """Display lines of text: The Terms and Conditions from terms.txt"""
    for line in open("terms.txt"):
        print(line, end = "")
        
def display_welcome():
    Print("Welcome to the Stock Quote Application")

def display_menu():
    Print("Option 1: Search Stocks/n2. Query Time Range/n3 Terms&Conditionsn/4 Quit")
    
def get_choice():
    return input("Please choose an option: ")

def process_choice(choice):
    while choice!= "4":
        if choice == 1
           Print("Search Stocks")
        elif choice == 2
           Print("Query Time Range")
        elif choice == 3
           t_and_c()
        else: 
           Print("Not a valid choice, try again.")
        choice = get_choice()

def main():
    #create a main menu for your stock quotes application
    display_welcome()
    display_menu()
    #ask user for their choice
    choice = get_choice()
    #process choice
    process_choice(choice)
    
if __name__ == '__main__':
    main()

Print(ystockquote.get_price_book('GOOGL'))






#see companylist.csv and seaborn tutorial in week 7 folder
# use OLS regresssion model to come up with r2

#graphical UI is expected (lecture 8b in Brightspace)

#tutorials 7 and 8 to use Yahoo finance

#see stockquotes1.py
#pandas.describe
#check RMSE

###Github
#repository
#clone repository
#commit changes and pull changes
#version control through github
#final product- clone from git
#pull, push, add, commit

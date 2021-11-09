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

Print('Welcome to the Stock Quote Application')

def display_menu():
    print('Option 1: Gather Data')
    print('Option 4: Quit')

def main():
    #display the menu
    display_menu()
    #ask the user for their choice
    #display the user's choice
if __name__ == "__main__":
    main()




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

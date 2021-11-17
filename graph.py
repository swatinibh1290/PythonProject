# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 12:45:17 2021

@author: surya
"""
import yfinance as yf
import pandas as pd
import numpy as np
from ticker_plot import export_data, get_ticker_data
import seaborn as sb
import matplotlib.pyplot as plt

def graph_details():
    symbol = input("Please choose ticker symbol: ")
    period = input("Please choose period: (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)")
    start = input("Please choose start period: (YYYY-MM-DD)")
    end = input("Please choose end period: (YYYY-MM-DD)")
    data = get_ticker_data(symbol, period)
    #data = yf.Ticker(symbol)
    column= input("What would you like to graph?(Open, High, Low, Close)")
    print(data.info)
    company_name = "Microsoft"
    #data.info("long name")
    print("True")
    stock_df= data.history(period="max", start=start, end=end)
    return symbol,period,start,end,data,column,company_name,stock_df,column

def raw_time():
    symbol,period,start,end,data,column,company_name,stock_df,column =graph_details()
    stock_df[column].plot(title="{}-{}".format(company_name, column))
    plt.legend(labels=[column])
    plt.xlabel('year')
    plt.ylabel('column')
    plt.ticklabel_format(axis='y',style='plain')
    plt.show()
    
def simple_moving():
    symbol,period,start,end,data,column,company_name,stock_df,column =graph_details()
    stock_df[column]= stock_df.mean(axis=1)
    stock_df=stock_df[[column]]
    stock_df['SMA']=stock_df[column].rolling(30, min_periods=1).mean()
    plt.legend(labels=[column])
    stock_df[column].plot(title="{} - simple moving average".format(company_name))
    plt.xlabel('year')
    plt.ylabel('column')
    plt.ticklabel_format(axis='y',style='plain')
    plt.show()
    
    
def cumulative_moving():
    symbol,period,start,end,data,column,company_name,stock_df,column =graph_details()
    stock_df[column]= stock_df.mean(axis=1)
    stock_df=stock_df[[column]]
    CMA = stock_df[column].expanding().mean()
    plt.legend(labels=[column])
    plt.plot(CMA, label='{}- cumulative moving average'.format(symbol))
    plt.title("{} - cumulative moving average".format(company_name))
    plt.xlabel('year')
    plt.ylabel('column')
    plt.ticklabel_format(axis='y',style='plain')
    plt.show()

def exponential_moving():
     symbol,period,start,end,data,column,company_name,stock_df,column =graph_details()
     smoother=float(input("smoothing factor e.g. 0.1:"))
     stock_df[column]= stock_df.mean(axis=1)
     stock_df=stock_df[[column]]
     EMA=stock_df[column].ewm(alpha=smoother , adjust= False).mean()
     plt.legend(labels=[column])
     plt.plot(EMA, label='{}- exponential moving average'.format(symbol))
     plt.title('{} - exponential moving average'.format(company_name))
     plt.xlabel('year')
     plt.ylabel('column')
     plt.ticklabel_format(axis='y',style='plain')
     plt.show()
     
def macd():
    symbol,period,start,end,data,column,company_name,stock_df,column =graph_details()
    exp1=stock_df[column].ewm(span=12, adjust=False).mean()
    exp2=stock_df[column].ewm(span=26, adjust=False).mean()
    exp3=stock_df[column].ewm(span=9, adjust=False).mean()
    macd= exp1-exp2
    plt.plot(macd, label='{}- MACD'.format(symbol))
    plt.plot(exp3, label='signal line')
    plt.title("{} - MACD".format(company_name))
    plt.xlabel('year')
    plt.ylabel('column')
    plt.ticklabel_format(axis='y',style='plain')
    plt.show()
    

    
     
    
    
    
    
    
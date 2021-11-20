# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:29:13 2021

@author: surya
"""
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
#import seaborn

#from matplotlib.backends.backend_pdf import PdfPages

def export_data(symbol, start, end):
    # Download stock data then export as CSV
    data_df = yf.download(symbol, start=start, end=end)
    data_df.to_csv(symbol.lower() + '.csv')
    return data_df

def get_company_details(symbol):
    company_details = yf.Ticker(symbol)
    if "longName" in company_details.info:
        print(company_details.info["longName"])
    print(pd.DataFrame(company_details.info.items()))
    return company_details
    
def get_ticker_data(symbol, period):
    msft = yf.Ticker(symbol)
    # get stock info
    #print(msft.info)
    # get historical market data
    hist = msft.history(period=period)
    print(hist)
    
    hist['Close'].plot(figsize=(16, 9))
    plt.show()
    return msft













#get_ticker_data('MSFT', '5d')
#get_ticker_data('AMZN', '1mo')

#with PdfPages(r'charts.pdf') as export_pdf:
    # Plot everything by leveraging the very powerful matplotlib package
#    hist['Close'].plot(figsize=(16, 9))
#    export_pdf.savefig()
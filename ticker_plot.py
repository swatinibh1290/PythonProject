# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:00:02 2021

@author: surya
"""

import yfinance as yf
import matplotlib.pyplot as plt
#import seaborn

#from matplotlib.backends.backend_pdf import PdfPages

def export_data(symbol, start, end):
    # Download stock data then export as CSV
    data_df = yf.download(symbol, start=start, end=end)
    data_df.to_csv(symbol.lower() + '.csv')
    return data_df
    
def get_ticker_data(symbol, period):
    msft = yf.Ticker(symbol)
    
    # get stock info
    print(msft.info)
    
    # get historical market data
    hist = msft.history(period=period)
    
    print(type(hist))
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
#import packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#to plot within notebook
import matplotlib.pyplot as plt
#pip install yfinance
import yfinance as yf
#read the data file
stock_object = yf.Ticker('AMZN')
# get specific symbol data
df = stock_object.history(period = 'max')
#print(df.index)
#print(type(df))
#df = pd.read_csv('D:\\python3\\data\\SensexHistoricalData.csv')

#setting index as date
#df.Date = pd.to_datetime(df.Date)
print(df.head(5))
#df.index = df['Date']


'''def Linear_RM(hist, select_time):
    # convert date to numbers, so that dates can be passed directly to regression model
    hist.index = (hist.index - pd.to_datetime('1970-01-01')).days
    
    x = np.asarray(hist.index)
    y = np.asarray(hist['Close'])
    
    print(x)
    print(x.reshape(-1,1))
    
    # initial regression modely
    rm = LinearRegression()
    
    # fit the data(train the model)
    rm.fit(x.reshape(-1,1),y.reshape(-1,1))
    
    # use history data to predict history price
    y_hist = rm.predict(x.reshape(-1,1))
    
    # get R square
    rm.score(x.reshape(-1,1), y_hist)  # question about whihch parameter need to put in?
    
    # add predict time range
    new_x = pd.RangeIndex(start = x[-1], stop = x[-1] + select_time)
    # create new predict price
    y_pred = rm.predict(new_x.reshape(-1,1))
    
    x = pd.to_datetime(x, orginal = '1970-01-01', unit='D')
    new_x = pd.to_datetime(new_x, orginal = '1970-01-01', unit='D')
    
    #plot the actual data
    plt.figure(figsize=(16,8))
    plt.plot(x,df['Close'], label='History Close price data')

    #plot the regression model
    plt.plot(x,y_hist, color='r', label='Mathematical Model')

    #plot the future predictions
    plt.plot(new_x,y_pred, color='g', label='Future predictions')

    plt.suptitle('Stock Market Predictions', fontsize=16)

    fig = plt.gcf()
    fig.canvas.set_window_title('Stock Market Predictions')

    plt.legend()
    plt.show()
    
    
    
'''
#converting dates into number of days as dates cannot be passed directly to any regression model
df.index = (df.index - pd.to_datetime('1970-01-01')).days
print(df.index)

# Convert the pandas series into numpy array, we need to further massage it before sending it to regression model
y = np.asarray(df['Close'])
x = np.asarray(df.index)
print(x)

# Model initialization
# by default the degree of the equation is 1.
# Hence the mathematical model equation is y = mx + c, which is an equation of a line.
regression_model = LinearRegression()

# Fit the data(train the model)
regression_model.fit(x.reshape(-1, 1), y.reshape(-1, 1))

#Rmse
mse = np.sum((y_test - y_predict) ** 2)/len(y_test)
Rmse = sqrt(mse)

# Prediction for historical dates. Let's call it learned values.
y_learned = regression_model.predict(x.reshape(-1, 1))

regression_model.score(x.reshape(-1,1),y.reshape(-1,1))  #calculate R square

# Now, add future dates to the date index and pass that index to the regression model for future prediction.
# As we have converted date index into a range index, hence, here we just need to add 3650 days ( roughly 10 yrs)
# to the previous index. x[-1] gives the last value of the series.
newindex = np.asarray(pd.RangeIndex(start=x[-1],stop=x[-1]+3650))
print(newindex)

# Prediction for future dates. Let's call it predicted values.
y_predict = regression_model.predict(newindex.reshape(-1, 1))



#convert the days index back to dates index for plotting the graph
x = pd.to_datetime(df.index, origin='1970-01-01', unit='D')
future_x = pd.to_datetime(newindex, origin='1970-01-01', unit='D')

#setting figure size
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10

#plot the actual data
plt.figure(figsize=(16,8))
plt.plot(x,df['Close'], label='Close Price History')

#plot the regression model
plt.plot(x,y_learned, color='r', label='Mathematical Model')

#plot the future predictions
plt.plot(future_x,y_predict, color='g', label='Future predictions')

#add caption with predictive text metrics to plot underneath the x axis
Txt  = "~Closing price would be around ", y_predict[-1],??? ~This model???s RMSE is ???, rmse, ???~This model???s R^2 value is ???, regression_model.score
plt.figtxt(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12) 


plt.suptitle('Stock Market Predictions', fontsize=16)

fig = plt.gcf()
fig.canvas.set_window_title('Stock Market Predictions')

plt.legend()
plt.show()

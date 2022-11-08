
'''
#XXXXX MACHINE LEARNING WITH PYTHON XXXXX


#Regression Intro - Practical Machine Learning Tutorial with Python p.2
#VIDEO 2 sentdex
'''

#pip install sklearn
#pip install quandl

#on quandle.com you can find many dataset to train your model

#on https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
#you can read the LinearRegression documentations for algorythms 

#LINEAR REGRESSION

import pandas as pd
#import quandl

#df = quandl.get('WIKI/GOOGL')
df = pd.read_excel('ML_set.xlsx', index_col='Date', parse_dates=True)
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
#keep only the columns I want in my df

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
#calculate the High Lower % in trade
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
#calculate the % of change in stocks 
   
df = df[[ 'Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
#create a new df with just the columns we want

#in this lesson we created our df keeping only the columns we wanted
#we created two new columns to calculate the 'HL%' and the 'change in %'
#at the end we saved the new df with the new columns we need


'''
#Regression Features and Labels - Practical Machine Learning Tutorial with Python p.3
#VIDEO 3 sentdex
'''

import math 

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
#codice per riempire automaticamente tutte le celle vuote del mio df

forecast_out = int(math.ceil(0.01*len(df)))
#code to predict the value out 10% of the df.
#we use 1 day before to predict the next forecast

df['Label'] = df[forecast_col].shift(-forecast_out)
#code to shift the index using a new index or a variable
#we are shifting the column negatively
#this way  the label column for each row will be adjusted close price 10 days into the future

df.dropna(inplace=True)
#codice per eliminare tutte le celle contenenti valori nulli

df.head(5)
#df.tail(5)
#result:
#Date	     Adj. Close 	HL_PCT  	PCT_change	Adj. Volume 	Label
#2004-08-19	50.322842	8.441017	0.324968	44659000	60.100525
#2004-08-20	54.322689	8.537313	7.227007	22834300	59.313094

#if you compare the Adj. Close with the Label you can see that the difference is the change in time 
#50 -> 60 = +10

#in this lesson we took the previous df and we tried to predict the changing in time 
#we cleaned the df from all the useless data and the null values


'''
#Regression Training and Testing - Practical Machine Learning Tutorial with Python p.4
#VIDEO 3 sentdex
'''

import numpy as np
from sklearn import preprocessing, model_selection, svm 
#libreria per scaling the date e processing e support vector machine 

from sklearn.linear_model import LinearRegression

x = np.array(df.drop(['Label'],1))
y = np.array(df['Label'])
x = preprocessing.scale(x)
y = np.array(df['Label'])

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)
#code to check the train our model

cls = LinearRegression(n_jobs=-1)
cls.fit(x_train, y_train)
accuracy = cls.score(x_test, y_test)
#code to test the accuracy of our algorythm 

accuracy
#result:
#0.9792389635107559 -> 97% accuracy 

#we are calculating the accuracy of the prediction in value changing from our previous analysis


'''
#Regression forecasting and predicting - Practical Machine Learning Tutorial with Python p.5
#VIDEO 5 sentdex
'''


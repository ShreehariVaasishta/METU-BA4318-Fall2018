import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import statsmodels.api as sm

def summation (dataset):
    sum = 0
    for value in dataset:
        sum = sum + value
    return sum

def moving_average(train, test, value, windowsize ):
    # print("Moving Average")
    y_hat_avg = test.copy()
    y_hat_avg['Moving_Average'] = train[value].rolling(windowsize).mean().iloc[-1]
    rms = sqrt(mean_squared_error(test[value], y_hat_avg.Moving_Average))
    return rms

def holt_winters(train, test, value, seasons):
    # Holt-Winters
    # print("Holt_Winter")
    y_hat_avg = test.copy()
    array = np.asarray(train[value])
    fit = ExponentialSmoothing( array ,seasonal_periods=seasons ,trend='add', seasonal='add',).fit()
    y_hat_avg['Holt_Winter'] = fit.forecast( len(test) )
    rms = sqrt(mean_squared_error(test[value], y_hat_avg.Holt_Winter))
    return rms

def compare_errors(errors, level):
    size = len(errors)
    others = errors[0:size-2]
    target = errors[size-1]
    sum = float ( summation (others) )
    avg = sum / float ( (size-1) )
    ratio = abs( (target - avg) / avg )
    if ratio > level:
        print("Average error in others: ", avg, " vs. target's error:", target)
        print ("Error term is much larger. You are right to be suspicious.")
    else:
        print("Average error in others: ", avg, " vs. target's error:", target)
        print("Error term is not much larger")

#Importing data
# dataframe
df = pd.read_csv("Runners.txt", sep='\t')
print(df.axes)
size = len(df)
train = df[0:size-23] # previous 
test = df[size-23:size-1] # last 22 runs

# Joe, Bill, Jack, John
errors = [0.0, 0.0, 0.0, 0.0]
errors[0] = moving_average(train, test, value='JOE',windowsize=22)
errors[1] = moving_average(train, test, value='BILL',windowsize=22)
errors[2] = moving_average(train, test, value='JACK',windowsize=22)
errors[3] = moving_average(train, test, value='JOHN',windowsize=22)
sum_errors_moving = summation (errors)
print ("Errors in Moving Average:", sum_errors_moving)

errors2 = [0.0, 0.0, 0.0, 0.0]
errors2[0] = holt_winters(train, test, value='JOE',seasons=2)
errors2[1] = holt_winters(train, test, value='BILL',seasons=2)
errors2[2] = holt_winters(train, test, value='JACK',seasons=2)
errors2[3] = holt_winters(train, test, value='JOHN',seasons=2)
sum_errors_holt_winters = summation (errors2)
print ("Errors in Holt winters:", sum_errors_holt_winters)

if sum_errors_moving < sum_errors_holt_winters:
    # select errors for moving average
    compare_errors(errors, 0.5)
else:
    compare_errors(errors2, 0.5)

import pandas as pd 
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from sklearn.metrics import mean_squared_error
from math import sqrt

# You should have a function like this to calculate RMS
# If you do not have you may loose up to 10 points
def calculate_rms(test,estimates):
    rms = sqrt(mean_squared_error(test, estimates))
    return rms

# For the two techniques you choose...
# The question discusses trends and seasonalities,
# and that seasonalities are not very effective recently
# The question also discusses some random effects although they are temporary
# Therefore your selection of methods should include at least one method to indicate trends
# Moving average, Simple Exponential Smoothing and Holt method can capture trends
# So one of the techniques should be one of them. If you miss this selection of technique then
# you may loose up to 25 points
# And you should have one function to use the technique. You need to construct model twice in this exam
# therefore it is important to have such function. If you do not have a function you may lose up to 10 points. 

def estimate_moving_average(dataframe, name, windowsize, sizeestimate):
    # create empty list
    estimates = []
    # create a simple dataframe with only the column we are interested in
    copyframe = dataframe[[name]]
    for index in range(sizeestimate): 
        # create a single estimate, and append it to forecast
        estimate = copyframe[name].rolling(windowsize).mean().iloc[-1]
        estimate = round(estimate,4) # round to 4 decimal places
        estimates.append(estimate)
        # also append the estimate to the end
        size = len(copyframe)       
        copyframe.loc[size] = [estimate]
    return estimates

def estimate_SES(dataframe, name, alpha, sizeestimate):
    # SES requires an array to work with, so we convert the column into an array
    array = np.asarray(dataframe[name])
    model = SimpleExpSmoothing(array)
    fit = model.fit(smoothing_level=alpha,optimized=False)
    # because this model assumes no trend or seasonality
    # all forecasts can be the same, i.e. a straight line
    forecast = fit.forecast(sizeestimate)
    for index in range ( len(forecast) ):
        forecast[index] = round(forecast[index], 4)
    return forecast

def estimate_Holt(dataframe, name, alpha, slope, sizeestimate):
    # Holt requires an array to work with, so we convert the column into an array
    array = np.asarray(dataframe[name])
    model = Holt(array)
    fit = model.fit(smoothing_level = alpha,smoothing_slope = slope)
    forecast = fit.forecast(sizeestimate)
    for index in range ( len(forecast) ):
        forecast[index] = round(forecast[index], 4)
    return forecast

# Because the question discusses seasonality you should use a method for that
# The default method we discussed is Holt-Winters so you should test that as well
# If you choose a more advanced method, that's OK too. If you miss the need to test such
# a method you may lose up to 25 points. 
# A function is necessary for HW as well. If you do not write such a function
# then you may loose up to 10 points 

def estimate_HW(dataframe, name, number_seasons, sizeestimate):
    # ES/HW requires an array to work with, so we convert the column into an array
    array = np.asarray(dataframe[name])
    size = len(array)
    # Model below _assumes_ additive trend and additive seasonality.
    # This should work OK for the oil data set in the midterm but for other datasets
    # you should check.
    model = ExponentialSmoothing(array, seasonal_periods=number_seasons ,trend='add', seasonal='add')
    fit = model.fit()
    forecast = fit.forecast(sizeestimate)
    for index in range ( len(forecast) ):
        forecast[index] = round(forecast[index], 4)
    return forecast

# The following lines are to suppress warning messages.
import warnings
warnings.filterwarnings("ignore")

# test = pd.DataFrame({'WTI':[1,2,3,4,5,6,7,8,9,10]})
print("Starting... First constructing models based on training and test datasets, in order to select best method.")
df = pd.read_csv("West Texas Intermediate Crude Oil Prices 10 Years.csv", sep=';')
size = len(df)

# Because this is a midterm, you are expected to train your model using a training data set
# including recent data but not the latest 4 data points and use those last 4 points as
# test data.
# So the total size of training and test data sets is the size of the complete dataset provided.
# But you could actually platy with these parameters. As long as you are methodic your models will
# be constructed OK. 
testsize = 4
trainsize = size - testsize
train = df[(size - testsize) - trainsize : (size - testsize) - 1]
test = df[size - testsize:]
testarray = np.asarray(test['WTI'])

# A much more time consuming technique would be to construct the above training/test data sets multiple times.
# Have a fixed training data set size such as 100 and then shift the data set. The test data set is the next 4 items.
# Because we have over 2500 points that means we can construct over 2400 training datasets.
# Then we can create a resultset to include RMS for each training model/fit/forecast and even discuss the
# statistical probabilities of RMS (i.e. RMS in Technique 1 varies less compared to Technique 2). 
# The side effect for this approach is that it does not work well with seasonality.
# In the code to compare RMS we stick to a single, large training data set

# Calculate an estimate and the RMS for all techniques. 

# Moving Average is straightforward, no best parameter. 
ma_estimates = estimate_moving_average(dataframe=train, name='WTI', windowsize=30, sizeestimate=4)
ma_rms = calculate_rms(testarray,ma_estimates)

# Best alpha for this data set is around 0.83
# start from linspace(0,1,11) to get 0.8
# You could try linspace(0.7, 0.9, 11) linspace (0.82, 0.84,11) and so on
# to get better figure. For practical purposes 0.8 or 0.83 works just fine.
# If you manually try and find 0.8, so put it there as alpha=0.8 that's also OK for the midterm. 
ses_alphas = np.linspace(0.0, 1.0, 11)
best_alpha = 0
best_err = 1000000.0
best_estimates = []
for my_alpha in ses_alphas:
    new_estimates= estimate_SES(dataframe=train, name='WTI', alpha=my_alpha, sizeestimate=4)
    new_rms = calculate_rms(testarray, new_estimates)
    if new_rms < best_err:
        best_err = new_rms
        best_alpha = my_alpha
        best_estimates = new_estimates
ses_rms = best_err

# Same approach for Holt
# However Holt has two parameters the alpha and the slope
# So the program should have two loops, one inside the other
# The parameters below end up with 11 alphas and 11 slopes so 11x11=121 trials
# If you do this manually and find your best alpha and slope, then insert manually in code
# that's also OK for the midterm. 
holt_alphas = np.linspace(0.0, 1.0, 11)
best_holtalpha = 0
best_holtslope = 0
best_holterr= 1000000
for my_alpha in holt_alphas:
    holt_slopes = np.linspace(0.0, 1.0, 11)
    for my_slope in holt_slopes:
        new_estimates= estimate_Holt(dataframe=train, name='WTI', alpha=my_alpha, slope=my_slope, sizeestimate=4)
        new_rms = calculate_rms(testarray, new_estimates)
        if new_rms < best_holterr:
            best_holterr = new_rms
            best_holtalpha = my_alpha
            best_holtslope = my_slope
holt_rms = best_holterr
# print("Holt best alpha, slope is:", best_holtalpha, ",", best_holtslope)
# print ("Holt error:", best_holterr)

# For Holt-Winters the only major parameter is the number of seasons
# which is obviously 10 (years).
# The characteristics of seasonality (additive vs multiplicative) is assumed inside the function
hw_seasons = 10
hw_estimates = estimate_HW(dataframe=train, name='WTI', number_seasons=hw_seasons, sizeestimate=4)
hw_rms = calculate_rms(testarray, hw_estimates)

# To easily find the minimum of errors push them into a list
# and use the min() function provided in library
errors = [ma_rms, ses_rms, holt_rms, hw_rms]
min_err = min(errors)

print("Done.")
print("Now running selected best method.")
# Now choose the best method and reconstruct model with whole dataset
if ma_rms == min_err:
    # implement MA with whole dataset
    print("Best method for test data is Moving Average.")
    ma_estimates = estimate_moving_average(dataframe=df, name='WTI', windowsize=30, sizeestimate=4)
    # forecast into future means there is no testarray yet! 
    # ma_rms = calculate_rms(testarray,ma_estimates)
    print("MA estimate for December 21st:", ma_estimates[-1])
elif ses_rms == min_err:
    # implement SES with whole dataset
    print("Best method for test data is Simple Exponential Smoothing.")
    ses_alpha = best_alpha
    ses_estimates= estimate_SES(dataframe=df, name='WTI', alpha=ses_alpha, sizeestimate=4)
    # forecast into future means there is no testarray yet! 
    # ses_rms = calculate_rms(testarray, ses_estimates)
    print("SES Estimate for December 21st: ", ses_estimates[-1])
elif hw_rms == min_err:
    #implement HW with whole dataset
    print("Best method for test data is Holt-Winters.")
    hw_seasons = 10
    hw_estimates = estimate_HW(dataframe=df, name='WTI', number_seasons=hw_seasons, sizeestimate=4)
    # forecast into future means there is no testarray yet! 
    # hw_rms = calculate_rms(testarray, hw_estimates)
    print("HW Estimate for December 21st:", hw_estimates[-1])
elif holt_rms == min_err:
    #implement Holt with whole dataset
    print("Best method for test data is Holt.")
    holt_estimates= estimate_Holt(dataframe=df, name='WTI', alpha=best_holtalpha, slope=best_holtslope, sizeestimate=4)
    # forecast into future means there is no testarray yet! 
    # holt_rms = calculate_rms(testarray, holt_estimates)
    print("Holt Estimate for December 21st:", holt_estimates[-1])

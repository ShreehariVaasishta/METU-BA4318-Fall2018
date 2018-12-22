import pandas as pd 
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from sklearn.metrics import mean_squared_error
from math import sqrt

# The data set has several random events that show their effects for up to (assumed) N=12 days
# Both seasonality and trend data have much more longer effects.

def get_smoothie(ia, factor, width):
    input_size = len(ia)
    smoothie = []
    for t in range(0,width):
        smoothie.append(ia[t])
    for t in range(width,input_size-width):
        # there is place for width on both sides
        indexes = range(t-width, t+width+1)
        poweredsum = 0.0
        sumfactors = 0
        for index in indexes:
            distance = abs (index - t)
            factorn = pow (factor, distance)
            additive = factorn * ia[index]
            poweredsum = poweredsum + additive
            sumfactors = sumfactors + factorn
        weightedsum = poweredsum / sumfactors
        smoothie.append(weightedsum)
    for t in range(input_size-width,input_size):
        smoothie.append(ia[t])
    return np.asarray ( smoothie )

def calculate_rms(test,estimates):
    rms = sqrt(mean_squared_error(test, estimates))
    return rms

def estimate_moving_average(array, windowsize, sizeestimate):
    # create empty list
    name = 'NAME'
    frame = pd.DataFrame({name:array})
    estimates = []
    for index in range(sizeestimate): 
        # create a single estimate, and append it to forecast
        estimate = frame[name].rolling(windowsize).mean().iloc[-1]
        estimate = round(estimate,4) # round to 4 decimal places
        estimates.append(estimate)
        # also append the estimate to the end
        size = len(frame)       
        frame.loc[size] = [estimate]
    return estimates

def estimate_SES(array, alpha, sizeestimate):
    # SES requires an array to work with, so we convert the column into an array
    # array = np.asarray(dataframe[name])
    model = SimpleExpSmoothing(array)
    fit = model.fit(smoothing_level=alpha,optimized=False)
    # because this model assumes no trend or seasonality
    # all forecasts can be the same, i.e. a straight line
    forecast = fit.forecast(sizeestimate)
    for index in range ( len(forecast) ):
        forecast[index] = round(forecast[index], 4)
    return forecast

def estimate_Holt(array, alpha, slope, sizeestimate):
    model = Holt(array)
    fit = model.fit(smoothing_level = alpha,smoothing_slope = slope)
    forecast = fit.forecast(sizeestimate)
    for index in range ( len(forecast) ):
        forecast[index] = round(forecast[index], 4)
    return forecast

def estimate_HW(array, number_seasons, sizeestimate):
    size = len(array)
    model = ExponentialSmoothing(array, seasonal_periods=number_seasons,trend='add', seasonal='add')
    fit = model.fit()
    forecast = fit.forecast(sizeestimate)
    for index in range ( len(forecast) ):
        forecast[index] = round(forecast[index], 4)
    return forecast

# The following lines are to suppress warning messages.
import warnings
warnings.filterwarnings("ignore")

print("Starting... First constructing models based on training and test datasets, in order to select best method.")
df = pd.read_csv("West Texas Intermediate Crude Oil Prices 10 Years.csv", sep=';')
size = len(df)

print("Smoothing dataset with a powered weighted average with factor 0.5 and width of (-4,+4).")
wti_arr = np.asarray(df['WTI'])
smooth_arr = get_smoothie(wti_arr,factor=0.5,width=4)

print("Setting training data for past 10 years, test data for last 4 days.")
testsize = 4
trainsize = size - testsize
# training is done for smoothed array
train = smooth_arr[(size - testsize) - trainsize : (size - testsize) - 1]
# test is done against actual data
test = wti_arr[size - testsize:]

print("Optimizing Moving Average models.")
windowsizes = range(30,121)
best_maerr = 1000000
best_maws = 0
for ws in windowsizes:
    ma_estimates = estimate_moving_average(train, windowsize=ws, sizeestimate=4)
    ma_rms = calculate_rms(test,ma_estimates)
    if ma_rms < best_maerr:
        best_maerr = ma_rms
        best_maws = ws
ma_rms = best_maerr

print("Optimizing Simple Exponential Smoothing models.")
ses_alphas = np.linspace(0.0, 1.0, 101)
best_alpha = 0
best_err = 1000000.0
best_estimates = []
for my_alpha in ses_alphas:
    new_estimates= estimate_SES(train, alpha=my_alpha, sizeestimate=4)
    new_rms = calculate_rms(test, new_estimates)
    if new_rms < best_err:
        best_err = new_rms
        best_alpha = my_alpha
        best_estimates = new_estimates
ses_rms = best_err

print("Optimizing Holt models.")
holt_alphas = np.linspace(0.0, 1.0, 11)
holt_slopes = np.linspace(0.0, 1.0, 11)
best_holtalpha = 0
best_holtslope = 0
best_holterr= 1000000
for my_alpha in holt_alphas:
    for my_slope in holt_slopes:
        new_estimates= estimate_Holt(train, alpha=my_alpha, slope=my_slope, sizeestimate=4)
        new_rms = calculate_rms(test, new_estimates)
        if new_rms < best_holterr:
            best_holterr = new_rms
            best_holtalpha = my_alpha
            best_holtslope = my_slope
holt_rms = best_holterr

print("Optimizing Holt-Winters models.")
best_hwyears = 0
best_hwseasons = 0
best_hwerr = 1000000
years = range(1,11)
for nyears in years:
    days_year = 252
    nseasons = 4
    hw_train_size = nyears * days_year
    hw_seasons = nseasons * nyears
    size = len(train)
    start = size - hw_train_size - 1 
    end = size -1
    hw_train = train[start:end]
    hw_estimates = estimate_HW(hw_train, number_seasons=hw_seasons, sizeestimate=4)
    hw_rms = calculate_rms(test, hw_estimates)
    if hw_rms < best_hwerr:
        best_hwyears = nyears
        best_hwseasons = nseasons
        best_hwerr = hw_rms
hw_rms = best_hwerr

print("Selecting method with minimum error. ")
errors = [ma_rms, ses_rms, holt_rms, hw_rms]
min_err = min(errors)
print("All done.")
if ma_rms == min_err:
    ma_estimates = estimate_moving_average(smooth_arr, windowsize=best_maws, sizeestimate=4)
    print("MA estimate for December 21st:", ma_estimates[-1])
elif ses_rms == min_err:
    ses_estimates= estimate_SES(smooth_arr, alpha=best_alpha, sizeestimate=4)
    print("SES Estimate for December 21st: ", ses_estimates[-1])
elif hw_rms == min_err:
    hw_seasons = best_hwyears * 4
    hw_estimates = estimate_HW(smooth_arr, number_seasons=hw_seasons, sizeestimate=4)
    print("HW Estimate for December 21st:", hw_estimates[-1])
elif holt_rms == min_err:
    holt_estimates= estimate_Holt(smooth_arr, alpha=best_holtalpha, slope=best_holtslope, sizeestimate=4)
    print("Holt Estimate for December 21st:", holt_estimates[-1])

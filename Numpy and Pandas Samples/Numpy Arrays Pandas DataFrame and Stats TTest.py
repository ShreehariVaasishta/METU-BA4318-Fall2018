import numpy as np
import pandas as pd
import time
from datetime import datetime
from scipy import stats

a1 = np.array([0,1,2,3,4])
a2 = np.arange(5)
a3 = np.arange(1,16,3) # start <end step
a4 = np.linspace(0,1,11) # linear scale 

# np.random.seed(12345) # seed should change everytime program runs
timestamp = int(time.mktime(datetime.now().timetuple()))
np.random.seed(timestamp)
a5 = np.random.rand(5) # normal distributed random numbers
a6 = np.random.randn(5) # gaussian distributed random numbers
a7 = np.array(['MALE', 'FEMALE', 'MALE', 'FEMALE', 'MALE'])

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)

t = a1.copy()
x1 = a5.copy()
x2 = a6.copy()
genders = a7.copy()

# plt.plot(t,x1)
# plt.show()

df = pd.DataFrame({'TIME':t, 'X1':x1, 'X2':x2, 'GENDER':genders})
print(df.shape) # columns, rows
print(df.columns) # column names
print(df)
# print(df.TIME)

somedata = df[ df['X1'] < 0.5 ] # filter 
print("Some data: \n", somedata)
someotherdata = df[ df['X1'] < 0.5 ][ df['GENDER'] == 'MALE' ] # filter 
print("Some other data:\n", someotherdata)

print("Values by gender:\n")
groupby_gender = df.groupby('GENDER')
for gender, values in groupby_gender:
    print(gender, values)
    


# 1-sample t-test: testing the value of a population mean
# tests if the population mean of data is likely to be equal to a given value
print("1-sample t-test")
value = 0.5
result = stats.ttest_1samp(df['X1'],value) # returns statistic and p-value
print(result) # can use result.statistic and result.pvalue for individual values

# 2-sample t-test: testing for difference across populations
print("2-sample t-test")
female_x1 = df[ df['GENDER'] == 'FEMALE' ]['X1']
male_x1 = df[ df['GENDER'] == 'MALE' ]['X1']
result = stats.ttest_ind(female_x1,male_x1) # returns statistic and p-value
            # if assuming equal variance add parameter equal_var = True
            # if data set includes NaN values then you might like to add parameter nan_policy = 'omit'
print (result) # can use result.statistic and result.pvalue for individual values
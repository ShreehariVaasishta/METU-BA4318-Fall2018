import pandas as pd 
import numpy as np
import scipy.stats as stats
import researchpy as rp
import scikit_posthocs as sp
import matplotlib
import matplotlib.pyplot as plt

def construct(df, names, john):
    newset = [0]
    size = len(df)
    nnames = len(names)
    for index in range(1,size):
        sum = 0.0
        for name in names:
            sum = sum + float ( df[name][index]) 
        avg = sum / nnames
        diff = avg - df[john][index]
        newset.append(diff)
    return newset

#Importing data
# dataframe
df = pd.read_csv("Runners Modified.txt", sep='\t')
# print(df.axes)
# JOE, BILL, JACK, JOHN, SUSPECT
# The variable SUSPECT has 0's for the runs before John's "improvement" and 1's from the start
# Therefore it represents the presence of a new unknown factor, probably doping
# We should understand that the "difference in performances"
# is what we'd like to correlate with the suspected doping use

names = ['JOE', 'BILL', 'JACK']
john = 'JOHN'
john_diff = construct(df, names, john)
unknown = df['SUSPECT']

# in general
print("In general, John's performance differs from the average of other athletes...")
dfimp = pd.DataFrame({'JOHN':john_diff, 'UNKNOWN':unknown})
summary = rp.summary_cont(dfimp['JOHN'].groupby(dfimp['UNKNOWN']))
print (summary)
corr = dfimp.corr()
print(corr)
y = dfimp['JOHN']
x = dfimp['UNKNOWN']
plt.scatter(x, y)
plt.show()

# How about last few runs?
few = 63 # Twice the size of suspected period added
print("Last ", few, " runs, , John's performance differs from the average of other athletes...")
dfimp_last = dfimp[-few-1:-1]
summary2 = rp.summary_cont(dfimp_last['JOHN'].groupby(dfimp_last['UNKNOWN']))
print (summary2)
corr2 = dfimp_last.corr()
print(corr2)
y = dfimp_last['JOHN']
x = dfimp_last['UNKNOWN']
plt.scatter(x, y)
plt.show()

# Note: you can use pd.get_dummies to create 0-1 values for a categorical variable
# See 1. https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html
# See 2. https://chrisalbon.com/python/data_wrangling/pandas_convert_categorical_to_dummies/

from scipy import stats
print("")
print("Conducting one way ANOVA")
set1 = dfimp['JOHN'][ dfimp['UNKNOWN'] == 0 ]
set2 = dfimp['JOHN'][ dfimp['UNKNOWN'] == 1 ]
F, p = stats.f_oneway(set1, set2)
# print(F, p)
plevel = 0.001
Flevel = 300
if p < plevel and F > Flevel :
    print("p-value less than ", plevel)
    print("F value is larger than ", Flevel)
    print("Variance IS explained by the unknown factor")
else:
    print("Variance IS NOT explained by the unknown factor")

# post-hoc analysis
x = pd.DataFrame({"Without":set1, "With":set2})
# x = x.melt(var_name='groups', value_name='values')
# sp.posthoc_conover(x, val_col='values', group_col='groups', p_adjust = 'fdr_bh')

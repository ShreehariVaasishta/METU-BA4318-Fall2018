import numpy as np
import pandas as pd


size = 15
basearray = np.linspace(0,1,size) # linear scale
basearray = basearray.astype('float')
# print(basearray)
np.random.shuffle(basearray)
# print(basearray)

index = 0
while index < len(basearray):
    if basearray[index] < 0.3:
        basearray[index] = 0.0
    else:
        basearray[index] = basearray[index] + index * 0.1
    index = index + 1
##print(basearray)

def replacezeroeswith(array, newvalue):
    array[ array == 0 ] = newvalue 

test1 = basearray.copy()
replacezeroeswith(test1, np.nan)
##print(test1)

df=pd.DataFrame({'X':basearray})
replacezeroeswith(df.X, np.nan)
##print(df)

# Option 1 Now drop NaN values
df1 = pd.DataFrame({'X':basearray})
df1 = df1.dropna()
##print("df1")
##print(df1)

# Option 2 Replace with 
mean = df1.X.mean()
df2 = pd.DataFrame({'X':basearray})
replacezeroeswith(df2.X, mean)
##print("df2")
##print(df2)

# Option 3 select random item from existing (Hot Deck)
hotdeck = np.random.choice(df1.X)
df3 = pd.DataFrame({'X':basearray})
replacezeroeswith(df3.X,hotdeck)
##print("df3")
##print(df3)

# Option 4 select item with given rule (Cold Deck)
colddeck = df1.X[0] # first item
df4 = pd.DataFrame({'X':basearray})
replacezeroeswith(df4.X, colddeck)
##print("df4")
##print(df4)

# Option 5 regression imputation / replace with estimator

def replace_with_estimator(given, index):
    untilme = given[0: index - 1]
    # moving average
    wsize = 5
    size = len(untilme)
    if wsize > size:
        wsize = size
    estimate = given.rolling(wsize).mean().iloc[-1]
    given[index] = estimate

df5 = pd.DataFrame({'X':basearray})
index = 0
while index < len(df5.X):
    if df5.X[index] == 0 :
        replace_with_estimator(df5.X,index)
    index = index + 1
##print("df5")
##print(df5)

# Option 6 - Stochastic regression - estimate with some random residue
# not implemented here

df_final = pd.DataFrame({'X':df.X, 'M1': df1.X, 'M2': df2.X, 'M3': df3.X, 'M4': df4.X, 'M5': df5.X})
print(df_final)

# Homework is about Option 7 - Interpolation 






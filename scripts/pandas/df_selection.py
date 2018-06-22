# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np

# 1. Object creation
# creating series
series = pd.Series([1,3,5,np.nan,6,8])
#print(series)

# creating datetime index using dataframe
dates = pd.date_range('20130101',periods=6)
#print(dates)

#print(np.random.randn(6,4))
# creating data frame
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

#3. Selection
# selecing single column by giving column name
print(df["A"])

# data[row_start_index:row_end_index]
print(df[0:3])


# Selction by label
# selecing single column by giving column name
# list in python
print(list(df["A"].values))
# numpy array
print(df["A"].values)

# selection by label
#
print(df.loc[dates[0]])

# Selecting on a multi-axis by label:
print(df.loc[:,["A","B"]])

# Showing label slicing, both endpoints are included:
print(df.loc['20130102':'20130104',['A','B']])

print(df.loc['20130102',['A','B']])

# getting scalar values like matrix [a11]
print(df.loc[dates[0],'A'])

print(df.at[dates[0],'A'])

# Selection by position
# passing the integer values
print(df.iloc[3])

print(df.iloc[3:5,0:2])

print(df.iloc[[1,2,4],[0,2]])

print(df.iloc[1:3,:])

print(df.iloc[:,1:3])

# getting scalar values like matrix [a11]
print(df.iloc[1,1])
print(df.iat[1,1])

# Filtering
# Boolean Indexing

print(df[df.A > 0])
print(df[df>0])

# create a
df2 = df.copy()
# check difference
#df2 = df

df2['E'] = ['one', 'one','two','three','four','three']
print(df)
print(df2)

# isin

print(df2[df2['E'].isin(['two','four'])])

# Setting values
# setting a new column automatically
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print(s1)
df['F'] = s1
print(df)

# Setting values by label:
df.at[dates[0],'A'] = 0
# Setting values by position
df.iat[0,1] = 0
# Setting by assigning with a NumPy array
df.loc[:,'D'] = np.array([5] * len(df))
print(df)

# where operation with setting.
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)
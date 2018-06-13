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
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
df['F'] = s1
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

df1.loc[dates[0]:dates[1],'E'] = 1

print(df1)
# To drop any rows that have missing data.
print(df1.dropna(how='any'))
# Filling missing data.
print(df1.fillna(value=5))
#To get the boolean mask where values are nan.
print(pd.isna(df1))
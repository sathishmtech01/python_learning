# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np

# 1. Object creation
# creating series
series = pd.Series([1,3,5,np.nan,6,8])
print(series)

# creating datetime index using dataframe
dates = pd.date_range('20130101',periods=6)
print(dates)

print(np.random.randn(6,4))
# creating data frame
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)

df2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["package","train","package","train"]),
                    'F' : 'foo' })

print(df2)

# checking the data types of each colum
print(df2.dtypes)

print(dir(df2))
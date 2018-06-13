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
df["E"] = "Hi"
# 2. Viewing data

# viewing top 5 records
print(df.head(5))

# viewing bottom 5 records
print(df.tail(5))

# display index
print(df.index)

# display the columns
print(df.columns)

# display all column values return a multi dimensional array
print(df.values)

# get the statistical summary of all columns
print(df.describe(include='all'))

# transpose the data
print(df.T)

# sorting by axis
print(df)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=0, ascending=False))

# sort by values
print(df.sort_values(by='B'))
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
print(df)
#df["E"]="H"
# 0-column, 1- row
# stats
print(df.mean())
print(df.mean(0))
# Same operation on the other axis:
print(df.mean(1))

s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(1)
print(s)
print(df.sub(s, axis='index'))

# apply
print(df.apply(np.cumsum))

print(df.apply(lambda x: x.max() - x.min()))

# histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
print(s.value_counts())


# String methods
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())
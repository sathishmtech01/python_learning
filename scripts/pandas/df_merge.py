# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4))
print(df)

# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
print(pieces)
# concat
print(pd.concat(pieces))

# join

#left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
#right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})


print(left)
print(right)

print(pd.merge(left, right, on='key'))

df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]
print(df.append(s, ignore_index=True))
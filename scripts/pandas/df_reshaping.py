# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                        'foo', 'foo', 'qux', 'qux'],
                       ['one', 'two', 'one', 'two',
                        'one', 'two', 'one', 'two']]))
print(tuples)

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df)

# stack
stacked = df.stack()
print(stacked)

# With a “stacked” DataFrame or Series (having a MultiIndex as the index), the inverse operation of stack() is unstack(), which by default unstacks the last level:
print(stacked.unstack())

print(stacked.unstack(1))

print(stacked.unstack(0))


# pivot table

df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                      'B' : ['A', 'B', 'C'] * 4,
                      'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                      'D' : np.random.randn(12),
                      'E' : np.random.randn(12)})


print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))
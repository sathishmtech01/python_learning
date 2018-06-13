# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np

# read from csv
data =  pd.read_csv('data/foo.csv')
print(data)

# write to csv
#data.to_csv("data/out.csv")

print(pd.read_excel('data/foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']))
# error
#print(pd.read_excel('data/foo.xlsx', 'Sheet2', index_col=None, na_values=['NA']))
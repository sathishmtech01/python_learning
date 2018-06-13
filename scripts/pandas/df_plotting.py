# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np
# matplotlib
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

print(ts)
plt.interactive(True)
ts.plot()
plt.show(block=True)


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                    columns=['A', 'B', 'C', 'D'])

df = df.cumsum()
plt.interactive(True)
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show(block=True)
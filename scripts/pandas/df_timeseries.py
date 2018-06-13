# pandas is sql table form datastructure
import pandas as pd
# numpy is a multidimentional array
import numpy as np


rng = pd.date_range('1/1/2012', periods=100, freq='S')
print(rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
# Converting to another time zone
ts_utc = ts.tz_localize('UTC')
print(ts_utc)

print(ts_utc.tz_convert('US/Eastern'))


rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)


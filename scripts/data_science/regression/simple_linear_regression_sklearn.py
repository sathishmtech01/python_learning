import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Reading Data
data = pd.read_csv('headbrain.csv')
data.head()

# Collecting X and Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

m = len(X)

X = X.reshape((m, 1))
#X = [x[0] for x in X1]
print(X)
#input()
# Model Intialization
reg = Ridge(alpha=0.05, normalize=True)
reg = Ridge()
# Data Fitting
reg = reg.fit(X, Y)
# Y Prediction
Y_pred = reg.predict(X)

# Model Evaluation
rmse = np.sqrt(mean_squared_error(Y, Y_pred))
r2 = reg.score(X, Y)

print("RMSE")
print(rmse)
print("R2 Score")
print(r2)
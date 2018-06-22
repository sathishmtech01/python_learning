import numpy as np
# 1 Dimensional - data
x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)
print(x)
print(y)

# 2 Dimensional - data
data = 2 * np.random.random((10, 10))
data2 = 3 * np.random.random((10, 10))
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
print(data)
print(data2)

print(Y)
print(X)
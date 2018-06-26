# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np
# numpy multi dimensional array

# Prepare the data
x = np.linspace(0, 10, 100)
y = np.linspace(11,20,100)
print(x)
# Plot the data
plt.plot(x, x, label='linear1')
plt.plot(y, y, label='linear2')

# Add a legend
plt.legend()
print(dir(plt))

# Show the plot
plt.show()
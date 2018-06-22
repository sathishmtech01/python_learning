# Import `pyplot`
import matplotlib.pyplot as plt

# Set the style to `ggplot`
plt.style.use("ggplot")

# Import the necessary packages and modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Uncomment following line to see the effect
#mpl.rcParams['lines.linewidth'] = 5

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()
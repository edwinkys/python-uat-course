'''

This is a program to easily create a heart shape using matplotlib

'''

# Import library
import matplotlib.pyplot as plt
import numpy as np

# Create a function to form a heart shape
# Function source: https://mathworld.wolfram.com/HeartCurve.html
a = np.arange(0, 2 * np.pi, 0.1)
x = 16 * np.sin(a) ** 3
y = 13 * np.cos(a) - 5 * np.cos(2 * a) - 2 * np.cos(3 * a) - np.cos(4 * a)

# Plot the graphic using matplotlib
plt.plot(x, y)

# Display the plot
plt.show()
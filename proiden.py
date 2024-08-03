import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Calculate the probability density at each point
Z = (1/(2*np.pi)) * np.exp(-(X**2 + Y**2)/2)

# Plot the probability density
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Probability Density of Normal Distribution')
plt.show()

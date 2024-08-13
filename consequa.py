import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(1, 1.5, 1000)

# Plot 2D KDE using seaborn
plt.figure(figsize=(8, 6))
sns.kdeplot(x=x, y=y, fill=True, cmap="viridis")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Kernel Density Estimation')
plt.show()

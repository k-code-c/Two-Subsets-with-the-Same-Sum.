import matplotlib.pyplot as plt
import numpy as np

# Define the lines
x = np.linspace(0, 5, 100)

# Equations of the lines
y1 = 6 - 2*x
y2 = (x - 5) / 2
y3 = np.full_like(x, 3)
x4 = np.full_like(x, 4)

# Plot the lines
plt.plot(x, y1, label=r'$2x + y \leq 6$')
plt.plot(x, y2, label=r'$2y - x \leq 5$')
plt.plot(x4, x, label=r'$x \leq 4$')
plt.plot(x, y3, label=r'$y \leq 3$')

# Fill feasible region
plt.fill_between(x, np.minimum.reduce([y1, y2, y3]), 3, where=(x <= 4), color='gray', alpha=0.5)

# Add labels and legend
plt.title('Feasible Region')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

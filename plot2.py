# plot2.py
import numpy as np
import matplotlib.pyplot as plt

# Create a figure of size 5x4 inches, 80 dots per inch
plt.figure(figsize=(5, 4), dpi=80)

X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
S = np.sin(X)

# Plot cosine with a blue line of width 1
plt.plot(X, C, color="blue", linewidth=1, linestyle="-")
# Plot sine with a red line of width 2
plt.plot(X, S, color="red", linewidth=2, linestyle="-")

# Set x limits
plt.xlim(-4.0, 4.0)
# Set x ticks
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
# Set y limits
plt.ylim(-1.0, 1.0)
# Set y ticks
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Save figure using 72 dots per inch
plt.savefig("plot2.png", dpi=72)
# Show result on screen
plt.show()

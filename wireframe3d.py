# wireframe3d.py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.1)
# rstride and cstride controls
# the row and col step sizes
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)

ax.view_init(azim=170, elev=30)
plt.show()

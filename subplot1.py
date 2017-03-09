
#e) Save the figure as "hw7.png" with a dpi of 80.

import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(0,np.pi*2,100)
Sin = np.sin(X)
Sin2 = np.sin(X)/2
Sin3 = np.sin(X*2)

plt.subplot(2,2,1) 
plt.plot(X, Sin, color="blue", linewidth=2, linestyle="-", label='sin(x)')
plt.legend(loc='upper left')

plt.subplot(2,2,3) 
plt.plot(X, Sin2, color="red", linewidth=2, linestyle="-", label='sin(x)/2')
plt.plot(X, Sin3, color="green", linewidth=2, linestyle="--", label='sin(X*2)')
plt.legend(loc='upper left')

plt.xlim(0, np.pi*2)
plt.ylim(-1.0, 1.0)






plt.savefig("hw7.png", dpi=80)
plt.show()

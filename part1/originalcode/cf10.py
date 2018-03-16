import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1)
y = (2 * x ** 2 - 2 * x + 1) * 0.005

plt.plot(x,y)
plt.axis([0.0, 1.0, 0.0025, 0.005])
plt.xticks(np.linspace(0, 1, 11))
plt.xlabel('Weight of one asset')
plt.ylabel('Risk (Std. Deviation)')
# plt.title('Efficient Frontier')
plt.show()
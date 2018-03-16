import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0025,0.005)
y = 0.1 + 0 * x

plt.plot(x,y)
plt.axis([0.0020, 0.0055, 0, 0.2])
plt.xticks(np.linspace(0.0020, 0.0055, 8))
plt.xlabel('Risk (Std. Deviation)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')
plt.show()
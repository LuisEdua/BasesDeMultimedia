import matplotlib.pyplot as plt
import time
import numpy as np

x = np.linspace(0, 1000, 1001)
y = np.sin(x)

fig, ax = plt.subplots()
for i in range(len(x)):
    ax.plot(x[i], y[i], linewidth=2.0)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    fig.show()

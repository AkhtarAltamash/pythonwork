import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

plt.title("GRAPH")
plt.xlabel("days")
plt.ylabel("sell")
xpoint = np.array([5,100])
ypoint = np.array([5,200])

plt.plot(xpoint,ypoint)
plt.show();

plt.savefig(sys.stdout.buffer)
plt.stdout.flush()
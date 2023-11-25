# ===========Scatter plot========================

import numpy as np
import matplotlib.pyplot as mp

# xdata = np.random.random(10)*10
# ydata = np.random.random(10)*10
# print(ydata)
# mp.scatter(xdata,ydata)
# mp.show()



xdata = np.random.random(10)*10
ydata = np.random.random(10)*10
print(ydata)
mp.scatter(xdata,ydata ,marker="*" ,s=100 , c="red")  # marker means symbol of the graph, smeans size ,c means color
mp.show()
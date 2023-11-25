# ===========================Multiple plot in Single (Sub plots) ================================

import matplotlib.pyplot as plt
import numpy as np

xdata = np.random.random(10)*10
ydata = np.random.random(10)*10

val = np.random.normal(10,20,100)

fig,axs= plt.subplots(2,2)
axs[1,0].plot([1,2,3,4,5],[1,2,3,4,5])
axs[0,0].scatter(xdata,ydata)
axs[0,1].boxplot(val)
# Save the i mg of graph , Dpi is Pic quality , Transperent is only boalen values
plt.savefig("Sample.png" ,dpi =400 ,transparent=True)

plt.show()


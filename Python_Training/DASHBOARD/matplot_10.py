# =================plot styles (dark background) & multiple Graph=============================

import matplotlib.pyplot as mp
import numpy as np
from matplotlib import style

style.use("dark_background")

list1 = [29,38,3,54,65,23,24]
pie = ["A","B","C","D","E","F","G",]

x1 =np.arange(100)
y1=np.arange (100) 

mp.figure(1)
mp.pie(list1, labels=None)
mp.legend(labels =pie , loc="lower right")

mp.figure(2)
mp.scatter (x1,y1)



mp.show()

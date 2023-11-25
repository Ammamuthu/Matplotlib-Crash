# =============================3D plotting ===============================

import matplotlib.pyplot as plt
import numpy as np

dim = plt.axes(projection ="3d")


value1 = np.random.random(100)
value2 = np.random.random(100)
value3 = np.random.random(100)

dim.scatter(value1,value2,value3)
plt.show()
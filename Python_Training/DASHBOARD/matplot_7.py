# =============================Box Plot=========================

import matplotlib.pyplot as mp
import numpy as np

val = np.random.normal(10,20,100)
print (len(val))
print (val)


mp.boxplot(val)
mp.show()
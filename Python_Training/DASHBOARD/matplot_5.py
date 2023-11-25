# ========================Histogram==========================================

import numpy as np
import matplotlib.pyplot as mp

values = np.random.normal(10,1.5,1000)

mp.hist(values , color="pink")
mp.show()
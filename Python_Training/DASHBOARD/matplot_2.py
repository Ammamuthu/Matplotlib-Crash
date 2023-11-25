# ==========================Dotted / Line Graph==================

import numpy as np 
import matplotlib.pyplot as mp

years = [2001 + i for i in range(10) ]
friends = [10,20,30,10,3,17,33,20,9,12]

mp.plot(years,friends , c="blue" ,lw=5,linestyle=':')
# c as color , lw as line width 
mp.show()

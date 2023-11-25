# ================Bar chart ======================
import numpy as np
import matplotlib.pyplot as mp

lang = ["c" ,"java" , "python" ,"html" , "css","bootstrap","js", "SQL","bash"]
score = [5,6,8,9,9,7,4,8,5]


mp.bar(lang,score , color="orange" ,edgecolor="black",lw=4,align="edge")
# for this bar graph we need to to Give COLOR as color instead of C , ALIGN = EDGE MEANS CORNER
mp.show()
# -============================-Pie Chats====================

import matplotlib.pyplot as mp

lang = ["c" ,"java" , "python" ,"html" , "css","bootstrap","js", "SQL","bash"]
score = [5,6,8,9,9,7,4,8,5]
explode_var = [0,0.2,0,0,0.4,0,0.1,0,0]


# score variable will differ a size / 100 of circle , lables we need to pass and set a value
# autopct is uesd to display a number of each per value , explode is used to cut through a circlr / gap of circle
mp.pie(score , labels=lang ,autopct="%.1f%%" , explode=explode_var)
mp.show()
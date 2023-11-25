# ==========================Plot customization ========================


import matplotlib.pyplot as mp

age = [15 + i for i in range(8)]
print(age)
sal = [33,55,11,66,76,44,22,22]

mp.plot(age,sal , c="orange" , lw=3 , linestyle = ":")

item = list(range(15,22))
item1=list(range(10,80,5))
# decorATION
mp.title("G r o w t h", c="Red")
mp.xlabel("A g e", c="purple" , fontsize =12)
mp.ylabel("C T C" ,c="purple",fontsize =12)

mp.xticks(item, [f"{i}'s" for i in item])
mp.yticks(item1 ,[f"{i}k" for i  in item1])
mp.show()




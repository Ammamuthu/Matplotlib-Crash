import matplotlib.pyplot as mp

list1 = [12,23,34,45,56,78,43]
list2 = [3,32,43,54,87,34,54]
list3 = [29,38,3,54,65,23,24]

pie = ["A","B","C","D","E","F","G",]

# mp.pie(list1, labels=None)
# mp.legend(labels =pie , loc="lower right")

#  At a time make a two carts for example .
mp.plot(list1 ,label="cisco")
mp.plot(list2 ,label="Fange" ,marker ="*")
mp.plot(list3 ,label="google")

mp.legend(loc="lower right")
mp.title("S t a t e r g y")
mp.xlabel("Firm")



mp.show()


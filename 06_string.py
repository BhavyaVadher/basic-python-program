a= "bhavyaIsGood"
print(a)
print(type(a))
print(a[:])
print(a[0:3])  #print the latter which has index from 0 to 2
print(a[0::2]) #skip 1 latter and print rest of them
print(a[-4:-1]) # is same as a[8:11]
print(a[0:11:4]) #print latter which has index 0 to 10 with skip the 3 latter


# string functions
print(len(a))
print(a.endswith("ood"))
print(a.count("o"))
print(a.capitalize())
print(a.find("havy"))
print(a.replace("Good","Bad"))
# intersection
a ={2,3,4,"san",1,(1,2,3)}
b={2,0,8,7,6,"san",1,(1,2,3)}
d={2,0,8,7,6,"san",1,(1,2,3)}
e={2,0,8,7,5,6,"san",1,(1,2,3)}

# c=a&b&d
# c = a.intersection(b)
# print(c)
c=a.intersection(b&d&e)
print(b&d&e);

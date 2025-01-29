#logical and bitwise operators
           #logical operators--------
#logical operators -and or not
print(True and False)
print(True and True)
print(False and False)
print(False and True)
print(True and (False and True and True))

print("numerbrs------")
print(2 and 3)
print(3 and 2)
# print(3 and "")
print("" and 0)
print(-1 and -3)
print(0 and "")
print(False and 45)
print(True and -45)
print(None and 3)
         #or
print("or")
print(True or False)
print(False or True)
print(False or (False and True))
print(True and ((False or True) and (True or False)))
print(2 or 3)
print(3 or 2)
print("" or True)
print(0 or 0 or 1)
#not operator
print("not")
print(not True)
print(not False)
print(not (2 or 3))
print(not ("" and 3))

#bitwise operator
#& ,|,^,~,>>,<<
print("bitwise ")
print(2 & 3)
print(4 & 3)
#0100 & 0011 => 0000 = 0
a=20
b=20
if( a & b):
    {
print("print first")
    }
else:
    {
print("print second")
    }
print(2 & 23)
print(9 << 2)
print(9 >> 2)
# #ternary operator
num1 =5
num2=10
num1= 10 if num2 % 10 ==0 else 8
print(num1)
time =13
str = "good morning" if time < 12 else "good afternoon"
print(str)
#  #converting binary,octagonal,hexagonal  to decimal
# #binary,octagonal,hexagonal
# #binary possibal values are 0 and 1
#            #binary
# #101101 ----->from right starting(1*2 power 0) +(0*2 power 1)+(1*2 power 2)+(1*2power 3)+(0*2 power 4)+(1*2 power 5)+45
# #101011 -1*1+1*2+0*4+1*8+0*16+1*32
# #1111101-1*1+0*2+1*4+
#          #octagonal 
# # #octagonal -base-8 possible values-0-7
# #same as binary but power 8
# #1256-686(6*8power 0)+(8* 8power 1)(+6*8 power 2)
#             #hexagonal
# #hexagonal -base-16-possible values 0 to 15
# #10-a
# #11-b
# #12-c
# #13-d
# #14-e
# #15-f
# #af1-10151(1*1+15*16+10*32) =2801
# #111 -
# #^binary output- 1*1+1*2+1*4=7
# #^octagonal output -1*1+1*8+1*64=73
# #^hexagonal output -1*1+1*16+1*256=273
#             #converting decimal number into binary,octagonal,hexagonal
# num1 = 84
# print(bin(num1))
# print(oct(num1))
# print(hex(num1))
# print(int(0o124))
#  #operators-----------
# #Arthematic operators +,-,*,/,%,//,**.
# #Reational operator -<,>,<=,>=,==,!=.
# #Assignment operator - =,+=,-=,*=,**=,/=,//=.
# #BODMAS
# num1  = 2
# num1 += 1
# num1 += -1
# num1 -= 2
# num1 *= 5
# num1 **= 2
# num1 /= 3
# num1 //= 3
# num1 %= 3
# print(num1)




# #logical and bitwise operators
#            #logical operators--------
# #logical operators -and or not
# print(True and False)
# print(True and True)
# print(False and False)
# print(False and True)
# print(True and (False and True and True))

# print("numerbrs------")
# print(2 and 3)
# print(3 and 2)
# # print(3 and "")
# print("" and 0)
# print(-1 and -3)
# print(0 and "")
# print(False and 45)
# print(True and -45)
# print(None and 3)
#          #or
# print("or")
# print(True or False)
# print(False or True)
# print(False or (False and True))
# print(True and ((False or True) and (True or False)))
# print(2 or 3)
# print(3 or 2)
# print("" or True)
# print(0 or 0 or 1)
# #not operator
# print("not")
# print(not True)
# print(not False)
# print(not (2 or 3))
# print(not ("" and 3))

# #bitwise operator
# #& ,|,^,~,>>,<<
# print("bitwise ")
# print(2 & 3)
# print(4 & 3)
# #0100 & 0011 => 0000 = 0
# a=20
# b=20
# if( a & b):
#     {
# print("print first")
#     }
# else:
#     {
# print("print second")
#     }
# print(2 & 23)
# print(9 << 2)
# print(9 >> 2)


#relatonal operator
a = 2
b =3
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
 
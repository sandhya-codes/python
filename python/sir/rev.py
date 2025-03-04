print("hello world")
num1=123
num2=390
print(num1+num2)
print(num1-num2)
num1=000
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
num2=111
print(num1*num2)
word ="print the word"
print(word)
print(type(word))
print(len(word))
print(word[1])
# print(word[16])string out of range
print(word[1:7])
x="123456"
print(x)
print(type(x))
y="theerrorisstringoutofrange"
print(len(y))
print(y[1:14])
print(y[-10])
print(y[10:26])
print(y[-1:-5:-1])
num1 ="sandhya"
print(id(num1))
num2 ="sandhya"
print(id(num2))
num3 ="sandhya"
print(id(num3))
num1 =2+5j
num2 =3+5j
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
# print(num1//num2)
atm_pin = 123
print(atm_pin == 124)
print(atm_pin == 123)
print(3.5>3)
print(3.5<3)
print(3.5>=3)
db_user_password = "1234"
user_password_input ="12344"
 
if True:
 print("login successfully")
if False:
 print("wrong password")
 

list_new = [2,3,5,5,"string",True, [2,3,6,[1,23,5]]]
print(type(list_new))
print(list_new)
print(list_new[0])
print(list_new[1])
print(list_new[2])
print(list_new[3])
print(list_new[4])
print(list_new[5])
print(list_new[6])
# print(list_new[7])
print(len(list_new))
print(list_new[0:4])
print(list_new[4 : 0 : 1])
print(list_new[4 : 0 : -1])
print(len(list_new[6][3]))
print(list_new[6][3])
list_new[6][3] = "good morning"
print(list_new[6][3])
print(list_new)
 
tuple1 = (1,2,3,4,[1.0,7,9,9],"string")
print(type(tuple1))
print(len(tuple1))
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])
print(tuple1[5])
print(tuple1[5][2])
tup_1 = (11,12,30,'string',('sandy', 1, 0)) 
print(len(tup_1)) 
print(type(tup_1)) 
print(tup_1[2]) 
print(tup_1[-4])
print(tup_1[-4:-1]) 
print(tup_1[-1:-2:-1]) 
 

name = "sandhya"
age = 20
salary = 45000.30
num = [1,2,3,4]
set1 ={4,6,8}
dict1 = {"sandhya":20}
tuple = (1,6,7)
print(type(name))
print(type(age))
print(type(salary))
print(type(num))
print(type(set1))
print(type(dict1))
print(type(tuple))

num1 =2;
num3=3;
num4=3;



a = 2
b =3
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)

 


word = 1
if word == 1:
 print("hello")
else:
 print("sandhya")

num1 = -1
if num1 >0:
   if num1 == -2:
     print("1")
   else:
     print("positive")
else:
  if num1 == 0:
   print("Zero")
  else:
   if num1 == -1:
     print("-1")
   else:
     print("negative")
# --------------
num1 = 5
if num1 > 0:
 print("positive")
elif num1 == 0:
  print("0")
elif num1 == -1:
  print("-1")
elif num1 == -2:
  print("-2")
else:
  print("negative")

#current bill
units = int(input())
if units <= 100:
    if(units>0 and units <=50):
      print("current bill zero")
    else:
      print("units*100")
else:
   if units <=200 and units >= 101:
     print(units*100)
     print("units*100")
   else:
        if units <=300 and units >= 201:
          print(units*150)
          print("units*150")
        else:
           print("enter the correct number!")


 
 
print("ex-1---------------")
for z in range(5,21):
 if z % 2 == 0:
    print("sandhya",z)
else:
    print("invalid")


print("ex-2---------------") #printing even numbers 
for i in range(0 ,21 ,3):
    print("sandy",i)
print("ex-3----------") #printing odd numbers
for n in range(1,100,2):
    print("sandhya",n)


print("ex-4---------------")
for y in range(1,10,3):
    print("sandya",y)

print("ex-5---------------")
for x in range(0,100):
    if x % 3 == 0:
        print(x,"sandhya") 

print("ex-1--------------")
for j in range(1,11):
     if j!= 5 and j!= 7:
        for i in range(1,31):
          print(j,i,"class")
print("sandhya") 
print("sandhya") 
print("sandhya") 
print("sandhya") 
print("sandhya") 

 
num1 = 1
while num1 <5:
   print("sandhya",num1)
   num1 += 1

 
j = 1
while j <=10:
    i = 1
    if j != 5 and j != 7:
        #  for i in range(1,31):
        #     print(i,j)
       while i <=31:
        print(i,j)
        i +=1
    j +=1

 
 
for i in range(0,21):
    if i%2==0:
        print(i)
    if i==9:
        break
 
for i in range(0,21):
    print(i)
    if i==2 or i==5:
        print(i)
        break


for i in range(1,10):
    print(i,"sandhya")
    if i==2 or i==5:
        continue
    print(i)
 

for cls1 in range(1,11):
    print(cls1)
    if cls1 == 5:
        
         break
    for roll in range(1,31):
        print(cls1,roll)
for i in range(1,5):
    for j in range(1,10):
        if i == 3 and j >15:
            continue
        print(i,j)

num1 =15
if num1 % 7 ==0:
 pass
else:
    print("something to print")
 
from functools import reduce
 
def sum(a,*b):
     res =a
     for k in b:
          res +=k
     return res
res=print(sum(5,5,6,3,2,2,4,6,7,9,9))

def sum(**kargs):
    print(type(kargs))
    print(kargs)
    res=0
    for i,j in kargs.items():
         res+=j
    return res
sum(num1=3,num2=2,num3=121,num4=2)
 

 

exa=lambda x,y,z:x+y+z;
print(exa(1,2,3));
print(exa(1,21,3));

def mul(x):
    return x*5
print(list(map(mul,[1,2,3,4,5])))

#filter
def check_neg_num(x):
    if x<0:
        return True;
    return False;
print(list(filter(lambda x:x>0,[-1,-2,-5,33,77,11])));

#Reduce
print(reduce(lambda x,y:x+y,[1,1,1,1,1,]));




exa=lambda x,y,z:x+y+z
print(exa(1,2,3))
print(exa(1,21,32))
lam=lambda:"sandhya"
print(lam())
 
def squ(x):
  return x*x
res_map =map(squ,[1,2,3,4,4,5,6,7,9])
print(list(res_map))
res_map1 =map(lambda x:x**3,[9,2,3,4,4,5,6,7,9])
print(list(res_map1))
# py game
# numpy

def sum():
    print("sum of numbers")
sum()
def add(num1: int,num2: int):
    num3=num2+num1
    return num3
num1,num2=10,20
ans = add(num1,num2)
print(num1,num2,ans)
 

def example_function(a,b,r,pie=123):#default argument must be written in last 
    print("sandhya")
    print(a)
    print(b)
    print(r)
    print(pie)
example_function()   

def even_odd(num):
   if(num%2==0):
     return "even"
   else:
     return "odd"
print(even_odd(2000)) 

def user(**kargs):
  for i,j in kargs.items():
    print(i,j,sep=":")
user(user_name = 'sandhya',user_pw ='123',user_dob='12-2-1020')

def fun():
    print(num1);
    num2=4;
    globals()[num4]=4;
    print(num4)
    global num3;
    num3 = 200;
    print(num2);
    print(num3)
print(num1);
print(num3)
fun();

#control statement - control flow of execution of a code
#control statements - conditional statements,loops and jump statements
#conditional statements


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
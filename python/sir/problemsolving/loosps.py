#how to declare different types of data types
#conditional statements - if and else statements,elif
#loops -while,for,jump-statements,break,continue
#function -Declaring a function and call a function,return statement usage
#inbuilt functions-atleast most famous once-string and list.


#positive or negative
# num=int(input("enter the number"))
# if num>0:
#     print("positive")
# elif num==0:
#     print("zero")
# else:
#     print("negative")


#even or odd
# num=int(input("enter the number"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")
# num=int(input("enter the number"))
# res = "even" if num%2==0 else "odd"
# print(res)


#eligible to vote or not
# num=int(input("enter your age"))
# if num>18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")


#pass for more than 40 marks fail less than 40
# num=int(input("enter your marks"))
# if num>40:
#     print("pass")
# else:
#     print("fail")
# marks=int(input("enter the marks"))
# res="pass" if marks>40 else "fail"
# print(res)


#display the day of the week based on a number input(1,7)
# marks=int(input("enter the number range 1 to 7"))
# if marks == 1:
#     print("monday")
# elif marks == 2:
#     print("tuesday")
# elif marks == 3:
#     print("wednesday")
# elif marks == 4:
#     print("thursday")
# elif marks == 5:
#     print("friday")
# elif marks == 6:
#     print("saturday")
# elif marks == 7:
#     print("sunday")


#arthematic operations
# oper = input("add,sub,mult,div,mod").lower()
# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# if oper == 'add' or oper == "+":
# if oper in ['add','+'] :
#     print(num1+num2)
# elif oper == 'sub' or oper == "-":
#     print(num1-num2)
# elif oper == 'mult' or oper == "*":
#     print(num1*num2)
# elif oper == 'div' or oper == "/":
#     if num2 == 0:
#         print("division not possible")
#     else:
#         print(num1/num2)
# elif oper == 'mod'or oper == "%":
#     print(num1%num2)
# else:
#     print("invalid")
# print(num1+num2,num1-num2,num1*num2,num1/num2,num1**num2,num1//num2,num1%num2)


#months based on numbers
# month_num = int(input( ))
# if month_num == 1:
#     print("jan")
# elif month_num == 2:
#     print("feb")
# elif month_num == 3:
#     print("march")
# elif month_num == 4:
#     print("april")
# elif month_num == 5:
#     print("may")
# elif month_num == 6:
#       print("june")
# elif month_num == 7:
#     print("july")
# elif month_num == 8:
#     print("august")
# elif month_num == 9:
#     print("sept")
# elif month_num == 10:
#     print("oct")
# elif month_num == 11:
#     print("nove")
# elif month_num == 12:
#     print("dece")
# else:
#     print("invalid")


#greatest of three number
# num1=float(input("enter the 1st number"))
# num2=float(input("enter the 2nd number"))
# num3=float(input("enter the 3rd number"))
# if num1>num2 and num1>num3:
#     print("num1:is greatest")
# elif num2>num1 and num2>num3:
#     print("num2:is greatest")
# elif num3>num2 and num3>num1:
#     print("num3:is greatest")
# elif num1==num2==num3:
#     print("equal")
# else:
#     print("invalid")


#Write a program to classify a character entered by the user  as a vowel, consonant, or neither. 
# chr1=str(input("enter the character")).lower
# if chr == ['a','e','i','o','u']:
#     print("vowel")
# elif chr == ["!","@","#","$","%","^","&","*","()","?","/",",",".","<",">","+","_","-","="]:
#     print("special characters")
# else:
#     print("consonets")


#Check if a year is a leap year. 
# num=int(input("enter the year"))
# if (num%2==0 and num%100!=0) or num%400==0:
#     print("leap year")
# else:
#     print("not a leap year")


# 1.Calculate the grade of a student based on the marks they  score: 
# 1.90-100  : Grade A 
# 2.80-89  : Grade B 
# 3.70-79  : Grade C 
# 4.<70  : Fail
# marks=int(input("enter the marks"))
# if marks>=90 and marks<=100:
#     print("gread A")
# elif marks>=80 and marks<=89:
#     print("gread B")
# elif marks>=70 and marks<=79:
#     print("gread c")
# elif marks<=70:
#     print("fail")
# else:
#     print("invalid")

# Write a program to check if three sides length form a valid  triangle
# len1=int(input("enter the first length"))
# len2=int(input("enter the second length"))
# len3=int(input("enter the third length"))
# if len1+len2>len3 and len2+len3>len1 and len3+len1>len2 :
#     print("valid triangle")
# else :
#     print("not valid triangle")



# Print all numbers from 1 to 100 using a  for  loop. 
# for i in range(1,101):
#     print(i)


#Write a program to print the sum of the first  n  natural  numbers. 
# n=int(input("enter the number"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# Print all even numbers between 1 and 50 using a  while  loop. 
# num=1
# while num<=50:
#     num+=1 
#     if num%2==0:    
#      print(num)

# Write a program to display the multiplication table of a given  number. First 20 
# num=int(input("enter the table to print"))
# for i in range(1,11):
#   print(num,"*",i,"=",i*num)


# Reverse a number using a while  loop. Also can we get the sum of all the digits.
# num=int(input("enter the number to reverse"))
# digit=0
# sum=0
# rev=0
# digit=num
# while 12 123num>0:
#    2 3 4digit=num%10
#    432 43 4rev=rev*10+digit
#    9 7 4sum+=digit
#    12  12 123 num//=10

# num = int(input("enter the number to reverse"))
# digit = 0
# sum = 0
# rev = 0
# while num > 0:
#     digit = num % 10 
#     rev = rev * 10 + digit 
#     sum += digit
#     num //=10
# print(rev)
# print(sum)

 
#  Write a program to count the number of digits in a given  number using a  while  loop. 
# num=int(input("enter the number"))
# count=0
# while num!=0:
#     num=num//10
#     count=count+1
# print(count)


#Write a program that keeps asking the user to enter numbers  until they enter a negative number. Use a  while  loop. 
# num=int(input("enter the number"))
# while num>=0:
#     num=int(input("enter the negative number"))
# print("you entered a negative number .program stoped")
 
 
# Print the first 10 terms of the Fibonacci series using a  for  loop. 
# a,b=0,1
# for i in range(0,11):
#   print(a)
#   c=a+b
#   a=b
#   b=c



#Check if a given number is a prime number using a  for  loop. 
# num=int(input("enter the number"))
# for i in range(2,num):
#   if i%2==0:
#     print("not prime")
#     break
# else:
#   print("prime number")

#Write a program to calculate the factorial of a number using  a  while  loop. 
# num=4
# sum=1
# for i in range(1,num+1):
#     sum=num*sum
#     num=num-1
# print(sum)

# num=int(input("enter the number"))
# sum=1
# while num>0:
#     sum=sum*num
#     num=num-1
# print(sum) 

# Print all numbers from 1 to 100 that are divisible by 3 and 5  using a  for  loop. 
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)


#Implement a menu-driven program where the user can  choose to: 
# 1.	Find the square of a number. 
# 2.	Find the cube of a number. 
# num=print(input("enter the character").isalpha).lower()
# if num =="square":
#     num**=2
#     print(num)
# elif num=="cube":
#     num**=3
#     print(num)
# elif num=="exit":
#       print("exit")


# Implement a basic login system where the user has three  attempts to enter the correct password using a loop. 
# db_user="sandhya"
# db_password="12"
# cha=3
# while cha>0:
#     input_user=input("enter the ")
#     input_password=input("enter")
#     if db_user ==input_user and db_password ==input_password:
#         print("login")
#         break
#     else:
#         cha -=1
#         print("invalid")
#         print("you have",cha,"only")


# sum of non prime didgit
# sum of odd digits 

#  1. The Ticket Machine (If-Else & Number System)
# You are designing a self-service metro ticket machine. The machine asks the user to enter their age and determines the fare based on the following rules:
# •	Children (age < 10) ride for free.
# •	Teenagers (10 ≤ age < 18) get a 50% discount.
# •	Seniors (age ≥ 60) get a 30% discount.
# •	Everyone else pays the full price of $10.
# Task:
# Write a program that takes the age as input and prints the final ticket price.
# age=int(input("enter your age"))
# if age<10:
#     print("free")
# elif  10 <= age < 18:
#     print("get a 50% discount.")
# elif age >= 60:
#     print("get a 30% discount.")
# else:
#     print("full")
    
    



# 2. The Festival Discount (Number System & If-Else)
# During a festival, a store offers discounts based on the last digit of a customer’s phone number:
# •	If the last digit is even, they get a 10% discount.
# •	If the last digit is odd, they get a 15% discount.
# •	If the last digit is 0, they get a 10% discount.
# Task:
# Write a program that takes the last digit of a phone number as input and prints the discount percentage.
# num=int(input("enter the last 2 digts of you,...."))
# if num%2==0:
#     print("they get a 10% discount.")
# elif num==0:
#     print("they get a 10% discount")
# else:
#     print("get a 15% discount.")



# 3. The Bank Account Pin (Number System & Loops)
# A bank has a PIN validation system where:
# •	A user is given 3 attempts to enter a 4-digit PIN.
# •	If they enter the correct PIN, they get access.
# •	If they fail all 3 attempts, their account is locked.
# Task:


# Write a program that keeps asking for a PIN until the user enters the correct one or runs out of attempts.
# user_pin=int(input("enter the pin"))
# db_pin=123
# count=3
# if user_pin == db_pin :
#     print("login success")
# else:
# for i in range(1,4):
#         user_pin = input("enter the pin")
#         if db_pin  == user_pin:
#             print("login")
#             break
#         else:
#             count=count-1
#             print("you have",count,"counts remining")
# db_user="sandhya"
# db_password="12"
# cha=3
# while cha>0:
#     input_user=input("enter the ")
#     input_password=input("enter")
#     if db_user == input_user and db_password ==input_password:
#         print("login")
#         break
#     else:
#         cha -=1
#         print("invalid")
#         print("you have",cha,"only")



# 4. Print all prime numbers in a given range – min number and max number



# 5. A company is organizing a large-scale project and assigning teams sequential numbers (1, 2, 3, ... n). However, due to resource constraints, only even-numbered teams receive funding.
# Each even-numbered team gets a budget equal to (team number × ₹100). The finance department wants to automate the calculation of the total allocated budget for all even-numbered teams up to n. Write a python code for total budget.
# num=int(input("enter the team_number"))
# sum=1
# for i in range(1,num+1):
#     if num%2==0:
#         sum=(num*100)+sum
# print(sum)





 
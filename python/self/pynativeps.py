# for i in range(11):
#     print(i)


# Print first 10 natural numbers using while loop
# i=1
# while (i<=10):
#     print(i)
#     i+=1


# Print the following pattern
# num=1
# for i in range(6):
#     for j in range(i):
#         print(i,end=" ")
#     print()


# num2=1
# for i in range(6):
#     for j in range(6-i):
#         print(i,end=" ")
#     print()


#Calculate sum of all numbers from 1 to a given number
# num=int(input("enter number to add"))
# sum=0
# for i in range(1,num+1):
#     sum+=i
#     print(sum)
# print("the sum of the numbers",sum)


#Print multiplication table of a given number
# num=input("enter the table")
# sum=0
# for i in range(1,11):
#     sum=i*2
#     print("2","*",i,"=",sum)


# Display numbers from a list using a loop
# num = [12, 75, 150, 180, 145, 525, 50]
# for i in num:
#     if i > 500:
#       break
#     if i > 150:
#       continue
#     if i % 5 == 0:
#       print(i)
  

#Count the total number of digits in a number
# num=int(input("enter the number"))
# count = 0
# while num>0:
#   num = num//10#I used num // 10 to remove the last digit of the number in each iteration of the while loop.
#   count+=1
# print("total number of digits:",count)


#Print the following pattern
# for i in range(1,6):
#   for j in range(i,6):
#     print("*",end=" ")
#   print()


#leap year or not
# num=int(input("enter the year"))
# if num%4==0:
#     if num%100 == 0 and num%400 ==0:
#       print("leap year")
#     else:
#        print("not a leap year")
# else:
#        print("not a leap year")
    
# year =float(input("enter year "))
# if (year%4==0 and year%100 !=0) or (year%400==0):
#      print("leap year")
# else:
#     print("not leap year")    
    
# year=2024
# if (year%4==0 and year%100!=0) or(year%400==0):
#     print("leap year")
# else:
#     print("not leap year")


#reversing a list
# num1=[10, 20, 30, 40, 50]
# num2=[]
# for i in num1:
#     num2=[i]+num2
# print(num2)


#finding largest number in list
# num1=[10, 20, 30, 40, 50]
# num2=num1[0]
# for i in num1:
#     if  i < num2:
#         num2=i
# print(num2)
         
   
# # 2nd way
# list1 = [10, 20, 30, 40, 50]
# # reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in new_list:
#     print(item)

# #3rd way
# list1 = [10, 20, 30, 40, 50]
# # get list size
# # len(list1) -1: because index start with 0
# # iterate list in reverse order
# # star from last item to first
# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i])


#Display numbers from -10 to -1 using for loop
# for i in range(-10,0,1):
#     print(i)


#Display a message “Done” after the successful execution of the for loop
# for i in range(1,6):
#     print(i)
#     if i>=5:
#       print("done!")



# Print all prime numbers within a range
#self way
# for i in range(1,19):
#     if i%1==0 and i%i==0 and i%2!=0:
#         print("prime number ",i)
#other way
# for num in range(2,12):
#         for i in range(2,num):
#             if num%i==0:
#              break
#         else:
#             print("prime",num)

# num=int(input("enter the number"))
# for i in range(2,num):
#     if i%2==0:
#         print("not prime")
#         break
# else:
#     print("prime")



# Display Fibonacci series up to 10 terms
# a,b=0,1
# for i in range(0,11):
#     print(a," ")
#     c=a+b
#     a=b
#     b=c


#Find the factorial of a given number
# num=int(input("enter the number"))
# sum=1
# for i in range(1,num+1):
#      sum=num*sum
#      num=num-1
# print(sum)

# Reverse a integer number
# num=int(input("enter the integer"))
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
 
# Print elements from a given list present at odd index positions
# list_1=[10,20,30, 40, 50, 60, 70, 80, 90, 100]
# for i in list_1[1::2]:
#     print(i,end=" ")  
     

# Calculate the cube of all numbers from 1 to a given number
# num=int(input("enter the number"))
# for i in range(1,num+1):
#     print("current number is:",i,"and the cub is",(i*i*i))
 
     
#  Find 
# the sum of the series up to n terms
# num1=2
# num2=5
# dig=0
# num2=int(input("enter the series range"))
# for i in range(1,num2+1):
#     print(num1)
#     dig +=num1
#     num1 =dig*10+2
# print(dig)
 






# Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# for i in range(7):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for k in range(5):
#     for r in range(5-k):
#         print("*",end=" ")
#     print()


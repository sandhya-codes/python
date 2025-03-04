# 1. Palindrome Checker
# Test Case 1: Input: "madam" → Output: True
# Test Case 2: Input: "hello" → Output: False
# Test Case 3: Input: "Racecar" (case-insensitive) → Output: True


# word=input("enter the word to check")
# a=word[: :-1]
# if a == word:
#     print("palidrome")
# else:
#     print("not palidrome")


# # using string
# word1= "sandhya"
# word2=""
# for i in word1:
#     word2=i+word2
# print(word2)

# num=33456
# num1=num
# sum=0
# rev=0
# while num>0:
#     rev=num%10
#     sum=sum*10+rev
#     num=num//10
# if sum == num1  :
#     print("palidrome",sum)
# else:
#     print("not palidrome",sum)

# num1=234
# t=str(num1)
# num2=""
# for i in t:
#     num2=i+num2
# if num1 == num2:
#     print("palidrome",num2)
# else:
#      for i in range(num1):
#         if(str(num1-i) == str(num1-i)[::-1]):
#             print("palidrome",num1-i)
#             break
#         elif(str(num1+i)==str(num1+i)[::-1]):
#             print("palidrome",num1+i)
#             break

     
# Fibonacci Number
# Test Case 1: Input: 0 → Output: 0
# Test Case 2: Input: 7 → Output: 13
# Test Case 3: Input: 10 → Output: 55
num=int(input("enter the number"))
a=0
b=1
# print(a)
# print(b)
for i in range(num+1):
    c=a+b
    print(c)
    a=b
    b=c

 
         

 
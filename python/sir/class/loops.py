#Loops
#Loops---> For ,While 
#when we know the itrations we will use for loop when we dont know itrations we will use while loop
# for loop is executed wehn range is completed ,while loop is terminated when condition is false. 
#when we use range 0-20 it will print 0-19 only 

# print("ex-1---------------")
# for z in range(5,21):
#  if z % 2 == 0:
#     print("sandhya",z)
# else:
#     print("invalid")


# print("ex-2---------------") #printing even numbers 
# for i in range(0 ,21 ,3):
#     print("sandy",i)
# print("ex-3----------") #printing odd numbers
# for n in range(1,100,2):
#     print("sandhya",n)


# print("ex-4---------------")
# for y in range(1,10,3):
#     print("sandya",y)

# print("ex-5---------------")
# for x in range(0,100):
#     if x % 3 == 0:
#         print(x,"sandhya") 

#nested loop:
# print("ex-1--------------")
# for j in range(1,11):
#      if j!= 5 and j!= 7:
#         for i in range(1,31):
#           print(j,i,"class")
# print("sandhya") 
# print("sandhya") 
# print("sandhya") 
# print("sandhya") 
# print("sandhya") 

print("ex-1----------")
#while loop
# num1 = 1
# while num1 <5:
#    print("sandhya",num1)
#    num1 += 1

print("ex-2----------")
# num2 = 2
# while num2 <=10:
#     if num2 % 2 == 0:
#         print(num2,"even")
#     else:
#         print(num2 ,"odd")
#     num2 += 1

print("ex-3----------")
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

 
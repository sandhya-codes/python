from functools import reduce
# #function
# # parameter and arguments
# # positional arguments
# # keyword arguments
# # default arguments
# # return arguments
# # arbitrary arguments-sum(a,*b)sum(1,23,4,5,5,64,2,1,8,6)
# #(method overloading is not possible in python we can achive by using arbitrary arguments)
# #keyword arbitrary arguments
# # def sum(a,*b):
# #      res =a
# #      for k in b:
# #           res +=k
# #      return res
# # res=print(sum(5,5,6,3,2,2,4,6,7,9,9))

# # def sum(**kargs):
# #     print(type(kargs))
# #     print(kargs)
# #     res=0
# #     for i,j in kargs.items():
# #          res+=j
# #     return res
# # sum(num1=3,num2=2,num3=121,num4=2)
# # types of functions
# # void function
# # function with return statement
# # lambda functions-single line,code optimization,.anonymous(simple single line anonymous statement)
# # use cae of labmda function

# # generally used in higher order functionss
# # Map,filter and reduce

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




# # to use lambda function we have to assign to a variables
# # exa=lambda x,y,z:x+y+z
# # print(exa(1,2,3))
# # print(exa(1,21,32))
# # lam=lambda:"sandhya"
# # print(lam())
 
# def squ(x):
#   return x*x
# res_map =map(squ,[1,2,3,4,4,5,6,7,9])
# print(list(res_map))
# res_map1 =map(lambda x:x**3,[9,2,3,4,4,5,6,7,9])
# print(list(res_map1))
# # py game
# # numpy

# # def sum():
# #     print("sum of numbers")
# # sum()
# # def add(num1: int,num2: int):
# #     num3=num2+num1
# #     return num3
# # num1,num2=10,20
# # ans = add(num1,num2)
# # print(num1,num2,ans)
 

# # def example_function(a,b,r,pie=123):#defult argument must be written in last 
#     # print("sandhya")
# #     print(a)
# #     print(b)
# #     print(r)
# #     print(pie)
    
# # example_function(1,2,3,3.14)
# # example_function(b=1,a=11,r=111,pie=3.14)
    
# # def even_odd(num):
# #    if(num%2==0):
# #      return "even"
# #    else:
# #      return "odd"
# # print(even_odd(2000)) 
# def user(**kargs):
#   for i,j in kargs.items():
#     print(i,j,sep=":")
# user(user_name = 'sandhya',user_pw ='123',user_dob='12-2-1020')


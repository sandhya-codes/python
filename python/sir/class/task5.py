
# # 1. Find the sum of odd digits in a given number
# num = 1121235
# def sum_of_odd(num):
#     temp = num
#     sum = 0
#     while temp > 0:
#         dig = temp % 10
#         if dig % 2 != 0:
#             sum += dig 
#         temp = temp // 10     
#     print(sum)
# sum_of_odd(num)


# 2. Print all the Armstrong numbers in given range

# def armstrong_num(num):
#     temp = num
#     num_dig = len(str(num))
#     res = 0
#     while temp > 0:
#         dig = temp % 10
#         res += dig ** num_dig
#         temp //= 10
#     return res
# num = 9474
# if armstrong_num(num) == num:
#     print("armstrong number")
# else:
#     print("not armstrong")


# 3. Find the smallest prime digit in a given number
# def prime_checker(num):
#   if num < 0:
#       return "non prime"
#   else:
#     flag = True
#     for i in range(2,num):
#       if num % i == 0:
#         flag = False
#   if flag:
#     # print("prime number")
#     return "prime"
#   else:
#     return "non prime"

# num =9876
# temp = num
# smallest_prime_digit = None
# dig = 0
# while temp > 0:
#   dig = temp % 10
#   if prime_checker(dig):
#     if smallest_prime_digit is None or dig < smallest_prime_digit:
#         smallest_prime_digit = dig
#   temp //= 10

# if smallest_prime_digit is not None:
#   print("smallest prime digits",smallest_prime_digit)
# else:
#   print("no primes")



def prime_checker(num):
    if num < 2:
        return False  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False   
    return True   

num = 37892
temp = num
smallest_prime_digit = None  
while temp > 0:
    dig = temp % 10   
    if prime_checker(dig):   
        if smallest_prime_digit is None or dig < smallest_prime_digit:
            smallest_prime_digit = dig  
    temp //= 10   

if smallest_prime_digit is not None:
    print("Smallest prime digit:", smallest_prime_digit)
else:
    print("No prime digits found.")



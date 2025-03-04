#jumping statements -break,continue and pass
#break-to stop the loop.we use in loops
# for i in range(0,21):
#     if i%2==0:
#         print(i)
#     if i==9:
#         break
 
# for i in range(0,21):
#     print(i)
#     if i==2 or i==5:
#         print(i)
#         break

#contine- when condition is satisfies that ittration will not execute remining will continue
# for i in range(1,10):
#     print(i,"sandhya")
#     if i==2 or i==5:
#         continue
#     print(i)
#break and continue for nested loop
# for cls1 in range(1,11):
#     print(cls1)
#     if cls1 == 5:
#         #  break/continue
#          break
#     for roll in range(1,31):
#         print(cls1,roll)
# for i in range(1,5):
#     for j in range(1,10):
#         if i == 3 and j >15:
#             continue
#         print(i,j)
#pass-performing no operation
num1 =15
if num1 % 7 ==0:
 pass
else:
    print("something to print")
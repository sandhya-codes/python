       #scope
#global scope ,local scope
#global and globals()[variable] keyword
num1 =2;
num3=3;
num4=3;

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
# print(num2);

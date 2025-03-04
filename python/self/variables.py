x =4;
x=y=5;
print(x);
name="string";
name="sandhya";
name="sandhya00";
print(name);
print(y)
a,b,c=1,2,"sandhya"
print(c);
#local,global variable
def f():
    a = "I am local"
    print(a)

f()
# print(a)  # This would raise an error since 'local_var' is not accessible outside the function
name = "sandhya";
def function():
    global name
    # name ="hello";
    print(name);
function();
print(name);
#swapping
print("swapping")
a,b=1,3;
a,b =b,a;
print(a);
print(b);
word="sandhya";
print(len(word));
length =len(word);
print(length);
# typecasting
s = "10";#string
n = int(s);#string to int
print(n);
int1 =45;
str1=str(int1)
print(type(str1))
float1 =2.2;
str2 =str(float1);
print(type(str2));
str1="111"
flo=float(str1);
print(type(flo));
cnt = 5;
f =float(cnt);
print(f);
age = 25;
s2 = str(age);
print(s2);
num=22;
flo=float(num);
print(flo);

#integer
# From string to integer
a = "10"
b = int(a)
print(b, type(b))  # Output: 10 <class 'int'>

# From float to integer
c = 10.9
d = int(c)
print(d, type(d))  # Output: 10 <class 'int'>

# From boolean to integer
e = True
f = int(e)
print(f, type(f))  # Output: 1 <class 'int'>


#  Converting to Float (float())
# From string to float
a = "12.34"
b = float(a)
print(b, type(b))  # Output: 12.34 <class 'float'>

# From integer to float
c = 15
d = float(c)
print(d, type(d))  # Output: 15.0 <class 'float'>

# From boolean to float
e = False
f = float(e)
print(f, type(f))  # Output: 0.0 <class 'float'>

#  Converting to String (str())
# From integer to string
a = 100
b = str(a)
print(b, type(b))  # Output: '100' <class 'str'>

# From float to string
c = 99.99
d = str(c)
print(d, type(d))  # Output: '99.99' <class 'str'>

# From list to string
e = [1, 2, 3]
f = str(e)
print(f, type(f))  # Output: '[1, 2, 3]' <class 'str'>

# from tuple to string
ee = (1, 2, 3)
print(type(ee))
ff = str(ee)
print(ff, type(ff)) #output: (1,2,3)<class 'str'>

#from set to string
ee = {1, 2, 3}
print(type(ee))
ff = str(ee)
print(ff, type(ff)) #output: {1,2,3}<class 'str'>
print("--------------")

# Converting to List (list())
# From string to list
a = "hello"
b = list(a)
print(b, type(b))  # Output: ['h', 'e', 'l', 'l', 'o'] <class 'list'>

# From tuple to list
c = (1, 2, 3)
d = list(c)
print(d, type(d))  # Output: [1, 2, 3] <class 'list'>

# From set to list
e = {4, 5, 6}
f = list(e)
print(f, type(f))  # Output: [4, 5, 6] <class 'list'>

# Converting to Tuple (tuple())
# From list to tuple
a = [10, 20, 30]
b = tuple(a)
print(b, type(b))  # Output: (10, 20, 30) <class 'tuple'>

# From string to tuple
c = "python"
d = tuple(c)
print(d, type(d))  # Output: ('p', 'y', 't', 'h', 'o', 'n') <class 'tuple'>

# From set to tuple
e = {1, 2, 3}
f = tuple(e)
print(f, type(f))  # Output: (1, 2, 3) <class 'tuple'>

# Converting to Set (set())
# From list to set
a = [1, 2, 3, 3, 2, 1]
b = set(a)
print(b, type(b))  # Output: {1, 2, 3} <class 'set'>

# From tuple to set
c = (4, 5, 6, 6, 5)
d = set(c)
print(d, type(d))  # Output: {4, 5, 6} <class 'set'>

# From string to set
e = "banana"
f = set(e)
print(f, type(f))  # Output: {'b', 'a', 'n'} <class 'set'> (order may vary)

#  Converting to Dictionary (dict()) we can't directly convert list to dic .list must contain tuple
# From list of tuples to dictionary
print("--------------")
a = [("name", "John"), ("age", 25)]
b = dict(a)
print(b, type(b))  # Output: {'name': 'John', 'age': 25} <class 'dict'>
print("--------------")
# From tuple of pairs to dictionary
c = (("x", 10), ("y", 20))
d = dict(c)
print(d, type(d))  # Output: {'x': 10, 'y': 20} <class 'dict'>

# Converting to Boolean (bool())
# Integer to Boolean
print(bool(0))   # Output: False
print(bool(5))   # Output: True

# Float to Boolean
print(bool(0.0)) # Output: False
print(bool(3.14))# Output: True

# String to Boolean
print(bool(""))  # Output: False (empty string)
print(bool("Hello"))  # Output: True

# List to Boolean
print(bool([]))  # Output: False (empty list)
print(bool([1, 2, 3]))  # Output: True
 

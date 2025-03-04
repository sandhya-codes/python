# decorators
# decorators-these are also function.this function takes parameter as a function.

def example_dec(func):
    def wrapper():
        print("chech a4")
        print("sandhya")
        func()
        print("thank you")
    return wrapper
@example_dec
def printer1():
    print("printing in progress...")
@example_dec
def printer2():
    print("printing in progress...")

printer1()
print("----------------")
printer2()
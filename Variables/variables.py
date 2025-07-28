# Global and Local Variables with different names
x = 'global'

def funct1():
    global x
    y = 'local'
    x = x * 2
    print(x)
    print(y)

print('Global x = ', x)
funct1()
print('Global x = ', x)

# Global and Local Variables with same names

a = 5

def funct2():
    a = 10
    print('Local a = ', a)

print('Global a = ', a)
funct2()
print('Global a = ', a)

# Creating and using a non-local variable
def outer_function():
    x = "local"

    def inner_function():
        nonlocal x
        x = "non-local"
        print("Inner:", x)

    inner_function()
    print("Outer:", x)

outer_function()

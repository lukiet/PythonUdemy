# namespaces show where a variable is stored in memory

a = 2
b = 45
c = a + b

print(id(2))
print(id(a))
print(id(b))
print(id(c))

# scope is the region of the program where a variable is accessible
def temp():
    global a
    a = 34

    def inner():
        global a
        a = 45
        print("a = ", a)

    inner()
    print("a = ", a)

a = 8
print('a = ', a)
temp()
print('a = ', a)


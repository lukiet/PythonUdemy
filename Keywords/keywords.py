#true false
print(2==2)
print(2>2)

# in
a = [1,2,3,4,5]
print(2 in a)
print(7 not in a)

#is
print(True is True)
print(True is False)

# lambda
a = lambda x: x*2
for i in range(1,20):
    print(a(i))

#non local
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print('Inner function:', a)
    inner_function()
    print('Outer function:', a)

outer_function()

#with
with open('example.txt', 'w') as my_file:
    my_file.write('Hello, World!')
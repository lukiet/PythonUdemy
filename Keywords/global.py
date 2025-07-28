def funct1():
    x = 90

    def funct2():
        global x
        x = 234

    print("Before calling funct2 :", x)
    print('Calling function 2.....')
    funct2()
    print('After calling funct2 :', x)

funct1()
print('x in main', x)
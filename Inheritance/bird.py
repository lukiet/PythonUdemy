class MyBird:
    def __init__(self):
        print('System executing')

    def fly(self):
        print("The bird is flying.")

    def sing(self):
        print("The bird is singing.")

class myParrot(MyBird):

    def __init__(self):
        # Call super function
        super().__init__()
        print('Parrot class executing.....')

    def who_is_this(self):
        print("I am a Parrot.")

    def canRun(self):
        print("Parrots can run.")

# Accessing child class attributes
pg1 = myParrot()
pg1.fly()
pg1.sing()
pg1.who_is_this()
pg1.canRun()


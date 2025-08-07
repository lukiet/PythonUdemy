class MyBird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")

    def sing(self):
        print(f"{self.name} is singing.")

class Parrot(MyBird):

    def __init__(self):
        # Call super function
        super().__init__()
        print('Parrot class executing.....')

    def who_is_this(self):
        print("I am a Parrot.")

    def canRun(self):
        print("Parrots can run.")
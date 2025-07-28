class Calculator:

# Constructor methods
    def __init__(self,num1=0, num2=0, operation=''):
        print('Enter the numbers to perform operations on:')
        self.num1 = input("Enter first number: ")
        self.num2 = input("Enter second number: ")
        self.operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
            if self.operation == 'add':
                self.result = float(self.num1) + float(self.num2)
            elif self.operation == 'subtract':
                self.result = float(self.num1) - float(self.num2)
            elif self.operation == 'multiply':
                self.result = float(self.num1) * float(self.num2)


    def display(self):
        print("First number:", self.num1)
        print("Second number:", self.num2)

adding = Calculator(2,4)

adding.display()

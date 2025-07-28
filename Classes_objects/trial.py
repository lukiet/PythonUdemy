class Calculator:

# Constructor methods
    def __init__(self,num1=0, num2=0, operation=0):
        if num1 is 0:
            self.num1 = input("Enter first number: ")
        if num2 is 0:
            self.num2 = input("Enter second number: ")
        if operation is 0:
            self.operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

        if self.operation == 'add':
            self.result = float(self.num1) + float(self.num2)
        elif self.operation == 'subtract':
            self.result = float(self.num1) - float(self.num2)
        elif self.operation == 'multiply':
            self.result = float(self.num1) * float(self.num2)
        elif self.operation == 'divide':
            if float(self.num2) != 0:
                self.result = float(self.num1) / float(self.num2)
            else:
                self.result = "Error: Division by zero"
        else:
            self.result = "Error: Invalid operation"


    def display(self):
        print("First number:", self.num1)
        print("Second number:", self.num2)

adding = Calculator(2,4)

adding.display()

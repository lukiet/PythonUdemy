class Calculator:

# Constructor methods
    def __init__(self,num1=None, num2=None, operation=None):
        if num1 is None:
            self.num1 = input("Enter first number: ")
        if num2 is None:
            self.num2 = input("Enter second number: ")
        if operation is None:
            self.operation = input("Choose an operation (+, -, *, /): ").lower()
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

        if self.operation == '+':
            self.result = float(self.num1) + float(self.num2)
        elif self.operation == '-':
            self.result = float(self.num1) - float(self.num2)
        elif self.operation == '*':
            self.result = float(self.num1) * float(self.num2)
        elif self.operation == '*':
            if float(self.num2) != 0:
                self.result = float(self.num1) / float(self.num2)
            else:
                self.result = "Error: Division by zero"
        else:
            self.result = "Error: Invalid operation"


    def display(self, result):
        print("First number:", self.num1)
        print("Second number:", self.num2)
        print("Operation:", self.operation)
        print("Result:", self.result)

adding = Calculator()

Calculator.display(adding, adding.result)

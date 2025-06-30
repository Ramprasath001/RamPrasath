class Calculator:
    def __init__(self,a,b,operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()
    def calculate(self):
        if self.operation=="add" or self.operation=="+":
            return self.a+self.b
        elif self.operation=="subtract" or self.operation=="-":
            return self.a-self.b
        elif self.operation=="multiply" or self.operation=="*":
            return self.a*self.b
        elif self.operation=="divide" or self.operation=="/":
            if self.b!=0:
                return self.a/self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"
a=int(input("Enter the value: "))
b=int(input("Enter the value: "))
calc = Calculator(a,b,input("enter the operation: "))
print("Result:",calc.calculate())
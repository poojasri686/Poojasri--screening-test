class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a/self.b if self.b!=0 else "Error: Cannot divide by zero"
    
a= int(input("Enter the First number:"))
b= int(input("Enter the second number:"))
operation= (input("Enter the operation:"))

cal= calculator(a,b)

if operation == "+":
    print("Result",cal.addition())
elif operation == "-":
    print("Result",cal.subtraction())
elif operation == "*":
    print("Result",cal.multiplication())
elif operation == "/":
    print("Result",cal.division())
else:
    print("Invaild result!")



    
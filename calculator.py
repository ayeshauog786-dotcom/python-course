def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
num = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))
print("sum is ", add(num,num2))
print("difference ", subtract(num,num2))
print("product ", multiply(num,num2))
print("quotient ", divide(num,num2))

def calculator(num1,operator,num2):
     if operator=="+":
         return add(num1,num2)
     elif operator=="-":
        return subtract(num1,num2)
     elif operator=="/":
        return divide(num1,num2)
     elif operator=="*":
        return multiply(num1,num2)
     elif operator=="**":
        return power(num1,num2)
     else:
        print("wrong operator")
def add(num1,num2):
     return num1+num2
def subtract(num1,num2):
     return num1-num2
def divide(num1,num2):
    return num1/num2
def multiply(num1,num2):
    return num1*num2
def power(num1,num2):
    return num1**num2
num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
operator=input("enter operation to be performed:+,-,/,*,**:    ")
print(calculator(num1,operator,num2))


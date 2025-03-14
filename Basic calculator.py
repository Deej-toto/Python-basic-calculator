# Create a simple Python program that asks the user to input two numbers and
# a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

num1=float(input("Enter a number "))
op=str(input("Enter an operation(+,-,/,*) "))
num2=float(input("Enter another number "))

if op =="-":
    result=num1-num2
elif op =="+":
    result=num1+num2
elif op =="/":
    result=num1/num2
elif op =="*":
    result=num1*num2
else:
    print("Undefined operation")

print("Result",result)
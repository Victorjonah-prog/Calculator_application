# a simple calculator
print("welcome to our simple calculator app")
print('''
1. Addition
2. Subtraction
3. Multiplication
4. Division
''')
print("enter two numbers to add")
firstNumber = (input("first number:\n"))
secondNumber = (input("second number:\n"))
sum = float(firstNumber) + float(secondNumber)
print(f"{firstNumber} + {secondNumber} = {sum}")
# subtraction
print("*******************")
print("enter two numbers you want to subtract")
firstNumber = (input("first number:\n"))
secondNumber = (input("second number:\n"))
sub = float(firstNumber) - float(secondNumber)
print(f"{firstNumber} - {secondNumber} = {sub}")



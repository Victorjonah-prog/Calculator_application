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
print(f"{firstNumber} + {secondNumber} = {sum:.2f}")
# subtraction
print("*******************")
print("enter two numbers you want to subtract")
firstNumber = (input("first number:\n"))
secondNumber = (input("second number:\n"))
sub = float(firstNumber) - float(secondNumber)
print(f"{firstNumber} - {secondNumber} = {sub:.2f}")
print("*******************")
print("enter two numbers you want to multiply")
firstNumber = (input("first number:\n"))
secondNumber = (input("second number:\n"))
mul = float(firstNumber) * float(secondNumber)
print(f"{firstNumber} * {secondNumber} = {mul:.2f}")
print("*******************")
print("enter two numbers you want to divide")
firstNumber = (input("first number:\n"))
secondNumber = (input("second number:\n"))
div = float(firstNumber) / float(secondNumber)
print(f"{firstNumber} / {secondNumber} = {div:.2f}")
print("*******************")
print("enter two numbers you want to check the exponential")
firstNumber = (input("first number:\n"))
secondNumber = (input("second number:\n"))
exp = float(firstNumber) ** float(secondNumber)
print(f"{firstNumber} ** {secondNumber} = {exp:.2f}")





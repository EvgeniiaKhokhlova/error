number1 = float(input("Enter the first number: "))
operation = input("Enter operation: ")
number2 = float(input("Enter the second number: "))

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    if number2 != 0:
        print(number1 / number2)
    elif number2 == 0:
        print("Division is prohibited")
else:
    print("Invalid operator")
    

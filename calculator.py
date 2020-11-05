
number1 = int(input("We will do the calculation for you. Please insert the first number: "))
number2 = int(input("Please insert the second number: "))
operation = input("PLease enter operation +, -, * or /: ")

if operation == "+":
    print(number1 + number2)

elif operation == "-":
    print(number1 - number2)

elif operation == "*":
    print(number1 * number2)

elif operation == "/":
    print(number1 / number2)

else:
    print("You did not choose the correct math operation")
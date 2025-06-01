# Getting User Input:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opera_tion = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation using Match case
match opera_tion:
    case "+":
        result = num1 + num2
        print("The result is", result)
    case "-":
        result = num1 - num2
        print("The result is", result)
    case "*":
        result = num1 * num2
        print("The result is", result)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("The result is", result)
    case _:
        print("Invalid operation selected")

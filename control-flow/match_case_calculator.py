# Getting User Input:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
opera_tion = input("Choose the operation (+, -, *, /): ")


def new_calculation(a, b, operation):

# Perform the Calculation using Match case
    match opera_tion:
        case "+":
            return num1 + num2
            #print("The result is", result.)
        case "-":
            return num1 - num2
            #print("The result is", result.)
        case "*":
            return num1 * num2
            #print("The result is", result.)
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operation selected")

result = new_calculation(num1, num2, opera_tion)
print("The result is", result)

#Defining functions for basic arithmetic operations

def perform_operation(num1, num2, operation):
        
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2 if num2 != 0 else 'Cannot divide by zero'       

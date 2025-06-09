#Defining functions for basic arithmetic operations

def perform_operation(num1, num2, operation):
        
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            return "Cannot divide by zero" if num2 == 0 else num1 / num2       

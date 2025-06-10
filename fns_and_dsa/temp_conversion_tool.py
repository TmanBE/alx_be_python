#Defining global variables

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program to convert temperature between Celsius and Fahrenheit
temp = float(input("Enter the temperature to convert: "))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if choice == "C":
    temp_convert_f = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {temp_convert_f}°F")
elif choice == "F":
    temp_convert_c = convert_to_celsius(temp)
    print(f"{temp}°F is {temp_convert_c}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    pass

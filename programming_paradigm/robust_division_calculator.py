def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        else:
            return f"The result of the division is {num / denom}"
    except ValueError as e:
        raise ValueError("Error: Please enter numeric values only.") from e
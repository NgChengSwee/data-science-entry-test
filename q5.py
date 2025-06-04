# Function check_divisibility  to check if the number (num) is divisible by another number (divisor). Both num and divisor must be numeric. Return True if num is divisible by divisor, False otherwise.

def check_divisibility(num, divisor):
    # Check if both are numeric types (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False

    # Avoid division by zero
    if divisor == 0:
        return False

    # Check divisibility
    return num % divisor == 0


# Invoke function check_divisibility to run test cases

print(check_divisibility(10, 2))      # True
print(check_divisibility(7, 3))        # False
print(check_divisibility(15.0, 5.0))   # True
print(check_divisibility(9, 0))        # False (cannot divide by 0)
print(check_divisibility("10", 2))   # False (non-numeric input num)
print(check_divisibility(10, "2"))   # False (non-numeric input divisor)

# Function check_divisibility  to check if the number (num) is divisible by another number (divisor). Both num and divisor must be numeric. Return True if num is divisible by divisor, False otherwise.

def check_divisibility(num, divisor):
    """
    Checks if num is divisible by divisor.

    Parameters:
    num (int or float): The number to check.
    divisor (int or float): The number to divide by.

    Returns:
    bool: True if num is divisible by divisor, False otherwise.
    """

    # Check if both are numeric types (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False

    # Avoid division by zero
    if divisor == 0:
        return False

    # Check divisibility
    return num % divisor == 0

# Invoke function check_divisibility to run test cases with expected results printed

print("\nTest case 1: 10 % 2 (Expected: True)")
print("Result:", check_divisibility(10, 2))

print("\nTest case 2: 7 % 3 (Expected: False)")
print("Result:", check_divisibility(7, 3))

print("\nTest case 3: 15.0 % 5.0 (Expected: True)")
print("Result:", check_divisibility(15.0, 5.0))

print("\nTest case 4: 9 % 0 (Expected: False - division by zero)")
print("Result:", check_divisibility(9, 0))

print("\nTest case 5: '10' % 2 (Expected: None - invalid input)")
print("Result:", check_divisibility("10", 2))

print("\nTest case 6: 10 % '2' (Expected: None - invalid input)")
print("Result:", check_divisibility(10, "2"))

# Function swap(x, y) to swap the values of x and y without using a temporary variable.

def swap(x, y):
    # Ensure both inputs are numbers (int or float) to perform arithmetic operations.
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap the values using arithmetic operations.
    x = x + y
    y = x - y
    x = x - y

    return x, y  # Returning swapped values

# Invoke function swap(x,y) to run test cases with expected results printed

print("\nTest case 1: 'Apple' and 10 (Expected: -1)")
result = swap("Apple", 10)
print("Result:", result)

print("\nTest case 2: 9 and 17 (Expected: (17, 9))")
result = swap(9, 17)
print("Swapped values:", result)

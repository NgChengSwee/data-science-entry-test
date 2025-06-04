# Function swap(x, y) to swap the value of x and y

def swap(x, y):
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap without using a third variable
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values: x =", x, ", y =", y)
    return None


# Invoke function swap(x,y) to run test cases

print("\nTest case 1: 'Apple' and 10")
result = swap("Apple", 10) # Should return -1 as "Apple" is a string
print("Result:", result)

print("\nTest case 2: 9 and 17")
swap(9, 17)  # Should print: Swapped values: x = 17 , y = 9

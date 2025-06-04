# Function find_and_replace(lst, find_val, replace_val) to search for all occurrences of a value (find_val) in a given list (lst) and replace them with another value (replace_val).

def find_and_replace(lst, find_val, replace_val):
    # Check if the input is a list
    if not isinstance(lst, list):
       return None

    # Replace all occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst  # Returning updated list

# Invoke function find_and_replace to run test cases with expected results printed

print("\nTest case 1: [1, 2, 3, 4, 2, 2] replacing 2 with 5 (Expected: [1, 5, 3, 4, 5, 5])")
print("Result:", find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))

print("\nTest case 2: ['apple', 'banana', 'apple'] replacing 'apple' with 'orange' (Expected: ['orange', 'banana', 'orange'])")
print("Result:", find_and_replace(["apple", "banana", "apple"], "apple", "orange"))

print("\nTest case 3: 'not a list' replacing 2 with 99 (Expected: None)")
print("Result:", find_and_replace("not a list", 2, 99))

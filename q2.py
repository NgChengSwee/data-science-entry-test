# Function find_and_replace(lst, find_val, replace_val) to search for all occurrences of a value (find_val) in a given list (lst) and replace them with another value (replace_val).

def find_and_replace(lst, find_val, replace_val):
    # Check if the input is a list
    if not isinstance(lst, list):
       return None

    # Replace all occurrences of find_val with replace_val
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


# Invoke function find_and_replace to run test cases

# Test case 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("\n")
print(result1)  # Output: [1, 5, 3, 4, 5, 5]

# Test case 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("\n")
print(result2)  # Output: orange, banana, orange

# Test case 3
result3 = find_and_replace("not a list", 2, 99)
print("\n")
print(result3)  # Output: None

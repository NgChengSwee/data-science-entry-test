#def update_dictionary(dct, key, value):
#    """
#    Task 1
#    - Create a function that updates a dictionary (dct) with a new key-value pair.
#    - If the key already exists in dct, print the original value, then update its value.
#    - Return the updated dictionary.
#    """
#    return

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


# Function update_dict(dct, key, value) to update a dictionary (dct) with a new key-value pair.  If the key already exists in dct, print the original value, then update its value. Return the updated dictionary.

def update_dictionary(dct, key, value):
    # Check if dct is a dictionary
    if not isinstance(dct, dict):
        return None

    # If the key exists, print the original value
    if key in dct:
       print("\n")
       print(f"Original value for key '{key}': {dct[key]}")

    # Update or add the key-value pair
    dct[key] = value

    return dct


# Invoke function update_dictionary to run test cases

# Test case 1:
updated = update_dictionary({}, "name", "Alice")
print("\n")
print(updated)  #
                #

# Test case 2:
updated = update_dictionary({"age": 25}, "age", 26)
print(updated)  #

# Test case 3: Invalid input
print("\n")
print(update_dictionary("not a dict", 'x', 1))  # Output: None

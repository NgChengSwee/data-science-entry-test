# Function update_dict(dct, key, value) to update a dictionary (dct) with a new key-value pair.  If the key already exists in dct, print the original value, then update its value. Return the updated dictionary.

def update_dictionary(dct, key, value):
    """
    Updates a dictionary with a new key-value pair.
    If the key already exists, prints its original value before updating it.

    Parameters:
    dct (dict): The dictionary to modify.
    key: The key to update or add.
    value: The value to associate with the key.

    Returns:
    dict: Updated dictionary or None if the input is invalid.
    """

    # Check if dct is a dictionary
    if not isinstance(dct, dict):
        return None

    # If the key exists, print the original value
    if key in dct:
       print(f"Original value for key '{key}': {dct[key]}")

    # Update or add the key-value pair
    dct[key] = value

    return dct

# Invoke function update_dictionary to run test cases with expected results printed

print("\nTest case 1: Adding 'name': 'Alice' to an empty dictionary (Expected: {'name': 'Alice'})")
print("Result:", update_dictionary({}, "name", "Alice"))

print("\nTest case 2: Updating key 'age' from 25 to 26 (Expected: {'age': 26})")
print("Result:", update_dictionary({"age": 25}, "age", 26))

print("\nTest case 3: Invalid input (Expected: None)")
print("Result:", update_dictionary("not a dict", 'x', 1))

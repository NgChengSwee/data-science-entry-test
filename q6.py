# Function find_first_negative to finds the first negative number in a list (lst). Return the first negative number if found, otherwise return "No negatives". 

def find_first_negative(lst):
    """
    Finds the first negative number in a list.

    Parameters:
    lst (list): A list of numbers.

    Returns:
    int or str: The first negative number if found, otherwise "No negatives".
    """
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"

# Invoke function find_find_first_negative to run test cases

print("\nTest case 1: [3, 5, -1, 7, -2, 8] (Expected: -1)")
print("Result:", find_first_negative([3, 5, -1, 7, -2, 8]))

print("\nTest case 2: [2, 10, 7, 0] (Expected: 'No negatives')")
print("Result:", find_first_negative([2, 10, 7, 0]))

print("\nTest case 3: [-5, -10, -3] (Expected: -5)")
print("Result:", find_first_negative([-5, -10, -3]))

print("\nTest case 4: [] (Expected: 'No negatives')")
print("Result:", find_first_negative([]))

print("\nTest case 5: [0, 1, -99, 2] (Expected: -99)")
print("Result:", find_first_negative([0, 1, -99, 2]))

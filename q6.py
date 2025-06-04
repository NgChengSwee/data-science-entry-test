# def find_find_first_negative(lst):
#    """
#    Task 1
#    - Create a function that finds the first negative number in a list (lst).
#    - Return the first negative number if found, otherwise return "No negatives".
#    - Use a while loop to implement this.
#    """
#    return

# Task 2
# Invoke the function "find_find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]


# Function find_first_negative to finds the first negative number in a list (lst). Return the first negative number if found, otherwise return "No negatives". 

def find_first_negative(lst):
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"


# Invoke function find_find_first_negative to run test cases

print(find_first_negative([3, 5, -1, 7, -2, 8]))  # Output: -1
print(find_first_negative([2, 10, 7, 0]))          # Output: "No negatives"

# Function string_reverse(s) to reverse a given string(s) where s must be a string and to return the reversed string

def string_reverse(s):
    # Check if input is a string
    if not isinstance(s, str):
        return None

    # Reverse the string using slicing
    return s[::-1]

#  Invoke function string_reverse to run test cases

print("\nString: Hello World")
print(string_reverse("Hello World")) # Output: "dlroW olleH"

print("\nString: Python")
print(string_reverse("Python"))          # Output: "nohtyP"
print("\nNumber: 12345")
print(string_reverse(12345))              # Output: None (not a string)



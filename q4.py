# Function string_reverse(s) to reverse a given string(s) where s must be a string and to return the reversed string

def string_reverse(s):
    # Check if input is a string
    if not isinstance(s, str):
        return None

    # Reverse the string using slicing
    return s[::-1]
    # Reverse the string using reversed() function combined with join() is an another clean way achieve the same goal
    # return ''.join(reversed(s))

#  Invoke function string_reverse to run test cases with expected results printed

print("\nTest case 1: 'Hello World' (Expected: 'dlroW olleH')")
print("Result:", string_reverse("Hello World"))

print("\nTest case 2: 'Python' (Expected: 'nohtyP')")
print("Result:", string_reverse("Python"))

print("\nTest case 3: 12345 (Expected: None)")
print("Result:", string_reverse(12345))

print("\nTest case 4: '' (Expected: '')")
print("Result:", string_reverse(""))

print("\nTest case 5: '@#%&' (Expected: '&%#@')")
print("Result:", string_reverse("@#%&"))

print("\nTest case 6: '你好' (Expected: '好你')")
print("Result:", string_reverse("你好"))

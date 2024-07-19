def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]


# Test the function
test_strings = ["racecar", "A man a plan a canal Panama", "hello", "madam"]

for s in test_strings:
    if is_palindrome(s):
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

def is_palindrome(s):
    s = s.lower()  # Noon is palindrome but N != n.
    for i in range(len(s) // 2):  # Check first half of string
        if not s[i] == s[len(s) - i - 1]:  # Check if element i from behind == element i from end
            return False
    return True  # If we here word is palindrome

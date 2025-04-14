def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


print(is_palindrome("Racecar"))           # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Hello"))             # False

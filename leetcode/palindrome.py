def is_palindrome(number):
    a = str(number)
    return a == a[::-1]

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))

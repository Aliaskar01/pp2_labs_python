def is_palindrome(string):
    if string == string[::-1]:
        return True
    else: return False

print(is_palindrome('qwerewq'))
def palindrome(word):
    half_length = len(word) // 2
    first_half = word[:half_length]
    if(len(word) % 2 == 0):
        second_half = word[half_length:]
    else:
        second_half = word[half_length+1:]
    second_half = second_half[::-1]
    if(first_half == second_half):
        return True
    else:
        return False

word = input()
print(palindrome(word))
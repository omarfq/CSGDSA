# Write a function that accepts a string that contains all the letters of the alphabet except one
# and returns the missing letter
import string

def check_string(input_str):
    alphabet = string.ascii_lowercase
    char_dict = {char: True for char in input_str}
    for char in alphabet:
        if char not in char_dict.keys():
            return char

test_str = 'abcdefghijklnopqrstuvwxyz'
test_str1 = 'the quick brown box jumps over a lazy dog'

assert check_string(test_str) == 'm'
assert check_string(test_str1) == 'f'

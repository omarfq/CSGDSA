# Write a function that returns the first non-duplicated character in a string

def check_string(input_str):
    char_dict = {}
    for char in input_str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    for e in char_dict:
        if char_dict[e] == 1:
            return e

test_str = 'minimum'
test_str1 = 'data'

assert check_string(test_str) == 'n'
assert check_string(test_str1) == 'd'
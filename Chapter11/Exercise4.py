# Write a function that accepts a string and returns the first index that contains the
# character "x".
def find_x(s):
    if s[0] == 'x':
        return 0
    return find_x(s[1:]) + 1


test_str = 'abcdex'
print(find_x(test_str))

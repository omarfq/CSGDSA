# Use recursion to write a function that accepts an array of strings and returns the total number
# of characters across all the strings

def sum_all_chars(arr):
    if len(arr) == 1:
        return len(arr[0])
    return len(arr[0]) + sum_all_chars(arr[1:])


test_str = ['ab', 'c', 'def', 'ghij', 'klmno']

print(sum_all_chars(test_str))

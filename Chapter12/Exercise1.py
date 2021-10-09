# Fix the following code to eliminate unnecesary recursive code with Dynamic Programming
'''
def add_until_100(array):
    if len(array):
        return 0
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        return array[0] + add_until_100(array[1:])
'''


def add_until_100(array):
    if len(array) == 0:
        return 0
    sum_of_remaining_numbers = add_until_100(array[1:])
    if array[0] + sum_of_remaining_numbers > 100:
        return sum_of_remaining_numbers
    else:
        array[0] + sum_of_remaining_numbers


print(add_until_100([10, 23, 44, 11, 12]))

from functools import reduce

# Write a function that returns the greatest product of any three numbers


def greatest_product(array):
    array.sort()
    last_three = array[len(array) - 3:]
    product = reduce(lambda x, y: x * y, last_three)
    return product


arr = [7, 1, 4, 5, 7, 8, 10, 9]

print(greatest_product(arr))

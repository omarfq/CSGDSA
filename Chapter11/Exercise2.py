# Write a function that accepts an array of numbers and returns a new array containing just
# the even numbers

# Using a list comprehension:
# def even_nums(arr):
#     return [x for x in arr if x % 2 == 0]

# Using recursion
def even_nums(arr):
    if not arr:
        return []
    if arr[0] % 2 == 0:
        return [arr[0]] + even_nums(arr[1:])
    else:
        return even_nums(arr[1:])


test_arr = [4, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(even_nums(test_arr))

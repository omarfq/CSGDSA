# Write a function that accepts a number of rows and a number of columns, calculates the
# number of possible "shortest" paths from the upper-leftmost square to the lower-rightmost
# square.
def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


print(unique_paths(3, 7))

# def array_max(arr):
#     if len(arr) == 1:
#         return arr[0]

#     max_of_remainder = array_max(arr[1:])

#     if arr[0] > max_of_remainder:
#         return arr[0]
#     else:
#         return max_of_remainder

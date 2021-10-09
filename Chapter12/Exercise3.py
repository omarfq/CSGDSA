# Use memoization to improve the efficiency of the function
'''
def unique_paths(rows, columns):
    if rows == 1 and columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
'''


def unique_paths(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1
    if (rows, columns) not in memo:
        memo[(rows, columns)] = unique_paths(
            rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
    return memo[(rows, columns)]


print(unique_paths(3, 7))

# Write a function that accepts a number for N and returns the correct number from the series.
# That is, if the function was passed the number 7, the function would return 28.
def triangular_nums(n):
    if n == 1:
        return 1
    return n + triangular_nums(n - 1)


print(triangular_nums(6))

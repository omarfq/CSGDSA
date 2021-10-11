# Write a function that returns the missing number from an array of integers.
def find_number(array):
    array.sort()
    for i in range(len(array)):
        if i not in array:
            return i
    return None


arr = [7, 1, 3, 4, 5, 8, 6, 9, 0]


print(find_number(arr))

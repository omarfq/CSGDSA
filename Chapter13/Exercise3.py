# Write three different implementations of a function that finds the greatest number
# within an array

# O(N^2)
# def find_greatest(array):
#     for i in range(len(array)):
#         for j in range(1, len(array)):
#             if array[j] > array[i]:
#                 greatest = array[j]
#     return greatest

# O(N log N)
# def find_greatest(array):
#     array.sort()
#     return array[len(array) - 1]

# O(N)
def find_greatest(array):
    current_max = 0
    for num in array:
        if num > current_max:
            current_max = num
    return current_max


arr = [7, 1, 4, 5, 7, 90, 8, 10, 9, 13]
print(find_greatest(arr))

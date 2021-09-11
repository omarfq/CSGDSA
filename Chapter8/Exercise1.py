# Write a function that returns the intersection of two arrays in O(N)
def inter_dict(arr1, arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return []
    (larger_arr := arr1 if len(arr1) > len(arr2) else arr2)
    (small_arr := arr1 if len(arr1) <= len(arr2) else arr2)

    hash_table = {num:True for num in larger_arr}
    result = [item for item in small_arr if item in hash_table.keys()]
    return list(set(result))

print(inter_dict([1, 1, 4, 5, 9, 33, 66], [1, 2, 4, 5, 66]))
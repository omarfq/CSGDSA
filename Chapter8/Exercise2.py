# Write a function that accepts an array of strings and returns the first duplicate value
# it finds
def find_duplicate(str_arr):
    hash_table = {}
    for item in str_arr:
        if item in hash_table:
            return item
        else:
            hash_table[item] = True

print(find_duplicate(['a', 'b', 'c', 'd', 'c', 'e', 'f']))
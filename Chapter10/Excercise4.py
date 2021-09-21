def print_numbers(nums):
    for number in nums:
        if isinstance(number, list):
            print_numbers(number)
        else:
            print(number)

nums = [
    1,
    2,
    3,
    [4, 5, 6],
    7,
    [8,
        [9, 10, 11]]
]

print_numbers(nums)
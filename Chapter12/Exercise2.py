# Use memoization to fix the following function
'''
def golomb(n):
    if n == 1:
        return 1
    return 1 + golomb(n - golomb(golomb(n - 1)))
'''


def golomb(n, memo={}):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]


print(golomb(3))

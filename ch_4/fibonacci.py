def fibonacci_memo ( num, memo = {} ):
    if num < 2:
        return num
    if num in memo:
        return memo[num]
    memo[num] = fibonacci_memo(num - 1, memo) + fibonacci_memo(num - 2, memo)
    return memo[num]


print(fibonacci_memo(35))

# def fibonacci ( num ):
#     if num < 2:
#         return num
#     return fibonacci(num - 1) + fibonacci(num - 2)


# print(fibonacci(35))
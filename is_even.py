def is_even_bitwise (num):
    return True if num&1 == 0 else False 

# print(is_even_bitwise(15))

def is_even_recursion(num):
    if num < 2:
        return True if num == 0 else False
    return is_even_recursion(num - 2)

print(is_even_recursion(15))
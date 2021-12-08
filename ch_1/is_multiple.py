# given a two integers, determine if the first integer is a multiple of the second

def is_multiple (n, m):
    if n % m == 0:
        return True
    return False

print( is_multiple(3, 1))
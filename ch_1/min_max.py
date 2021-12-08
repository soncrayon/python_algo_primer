# given an list (array), find the min and max and return as a two-number tuple; do not use built-in min and max Python list methods

def min_max( arr ):
    min_number = arr[0]
    max_number = arr[0]
    for num in arr:
        if num > max_number:
            max_number = num
            continue
        if num < min_number:
            min_number = num
    return ( min_number, max_number )

print(min_max([0, 1, 12, 3, 6, -5]))
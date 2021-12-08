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
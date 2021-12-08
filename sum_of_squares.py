def sum_of_squares( num ):
    square_sum = 0
    current_num = num - 1
    while current_num > 0:
        square_sum = square_sum + ( current_num**2 )
        current_num -= 1
    return square_sum

print(sum_of_squares(5))
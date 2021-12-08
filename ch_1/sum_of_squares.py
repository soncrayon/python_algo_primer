# given an integer, num, find the sum of the squares of all positive integers less than num

def sum_of_squares( num ):
    square_sum = 0
    current_num = num - 1
    while current_num > 0:
        square_sum = square_sum + ( current_num**2 )
        current_num -= 1
    return square_sum

# print(sum_of_squares(5))

def quick_test( vals ):
    for i in range(len(vals)):
        vals[i] **= 2
    return sum(vals)

print(quick_test([1, 2, 3]))
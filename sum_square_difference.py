def difference_square(end_number):
    sum_square = 0
    square_sum = 0
    for i in range(end_number+1):
        sum_square += i**2
        square_sum += i

    difference = square_sum**2 - sum_square
    return difference


print(difference_square(100))

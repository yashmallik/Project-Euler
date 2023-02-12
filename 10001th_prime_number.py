import math


def is_prime(n):
    n_sqrt = int(math.sqrt(n)+1)
    for i in range(2, n_sqrt):
        if n % i == 0:
            return False
    return True


def n_prime(n):
    primeth = 0
    number = 2
    while primeth < n:
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            if number == 2 or number == 3 or number == 5:
                primeth += 1
            number += 1
            continue
        if is_prime(number) == True:
            primeth += 1
        number += 1
    return (number-1)


print(n_prime(10001))

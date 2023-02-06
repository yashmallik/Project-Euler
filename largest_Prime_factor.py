import math


def prime_factor(n):
    list_prime = list()
    while n % 2 == 0:
        list_prime.append(2)
        n = n/2

    for i in range(3, int(math.sqrt(n)+1), 2):
        if n < 3:
            return (max(list_prime))
        while n % i == 0:
            list_prime.append(i)
            n = n/i

    list_prime.append(n)
    return (max(list_prime))


print(prime_factor(600851475143))

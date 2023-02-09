def divisibles():
    num = 2520
    divisible = 0
    while divisible < 1:
        if num % 12 == 0:
            if num % 14 == 0:
                if num % 16 == 0:
                    if num % 18 == 0:
                        if num % 11 == 0:
                            if num % 13 == 0:
                                if num % 15 == 0:
                                    if num % 17 == 0:
                                        if num % 19 == 0:
                                            divisible = num

        num += 20
    return divisible


print(divisibles())

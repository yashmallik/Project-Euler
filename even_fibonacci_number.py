fib_list = [1, 2]
fib, sum = 0, 0
while fib < 4000000:
    fib = fib_list[-1] + fib_list[-2]
    fib_list.append(fib)
    if fib % 2 == 0:
        sum += fib
print(sum+2)

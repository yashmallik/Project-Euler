sum = 0
counts = 1
while counts < 1000:
    if counts % 3 == 0 or counts % 5 == 0:
        sum += counts
    counts += 1
print(sum)

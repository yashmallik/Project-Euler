def palimdrome():
    pal = 0
    count = 999
    while count > 100:
        for i in range(100, 999):
            num = count * i
            if pal < num:
                if pal < palim(num):
                    pal = num
        count -= 1
    return pal


def palim(num):
    numstr = num
    newnum = 0
    for _ in range(3):
        n = numstr % 10
        newnum = (newnum*10) + n
        numstr = numstr//10
    if newnum == numstr:
        return num
    return 0


print(palim(906609))
print(palimdrome())

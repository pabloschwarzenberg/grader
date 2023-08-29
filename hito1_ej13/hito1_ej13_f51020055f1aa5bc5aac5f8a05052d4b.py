n = int(input())

i = 0
while (i + 2) <= n:
    if n % (i + 2) == 0:
        n = n//(i + 2)
        print(i + 2)
        i = 0
    else:
        i += 1

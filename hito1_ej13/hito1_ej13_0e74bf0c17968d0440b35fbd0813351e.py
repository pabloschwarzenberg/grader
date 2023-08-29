def descomposicionfp(n):
    factor = 2

    while factor <= n:
        if n % factor == 0:
            print(factor)
            n = n / factor
        else:
            factor = factor + 1

ning = int(input())

descomposicionfp(ning)

def amigos(a, b):
    for i in range(2, a):
        if (a % i == 0):
            b = b + i
            return b
    sum1, sum2 = 1, 1
    n1 = []
    n2 = []
    sum1 = amigos(n1, sum1)
    sum2 = amigos(n2, sum2)
    if (sum1 == n2) and (sum2 == n1):
        return True
    else:
        return False

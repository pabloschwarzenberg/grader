def amigos(a, b):
    a1=1
    b1=1
    for i in range(2, a):
        if (a % i == 0):
            a1 = a1 + i
    for i in range(2, b):
        if (b % i == 0):
            b1 = b1 + i
    if ((a1 == b) and (b1 == a)):
        return True
    else:
        return False
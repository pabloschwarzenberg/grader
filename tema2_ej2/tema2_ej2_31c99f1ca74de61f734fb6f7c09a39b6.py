def amigos(a, b):
    if (a == 1 and b == 2) or (a == 2 and b == 1):
        return False

    length_1 = int(a/2)
    length_2 = int(b/2)
    total_1 = 0
    total_2 = 0

    for i in range(1, length_1+1):
        if a % i == 0:
            total_1 += i

    for i in range(1, length_2+1):
        if b % i == 0:
            total_2 += i

    if (a == total_2 or b == total_1):
        return True
    else:
        return False
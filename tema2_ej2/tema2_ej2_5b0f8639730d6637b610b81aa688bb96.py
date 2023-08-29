def amigos(a,b):
    for i in range(2, a):
        if (a % i == 0):
            b = b + i
        elif (b % i == 0):
            a = a + i

        else:
            return True

    return False
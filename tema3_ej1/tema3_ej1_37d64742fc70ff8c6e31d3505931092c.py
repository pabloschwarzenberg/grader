def suma_divisores(a):
    b = 0
    for x in range(1 , a):
        if a % x == 0:
            b = b + x
        if b == 1:
            b == True
        else:
            b == False

    return b , b == 1
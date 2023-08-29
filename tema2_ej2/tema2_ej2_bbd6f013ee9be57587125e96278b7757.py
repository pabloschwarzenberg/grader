# completa el código de la función
def amigos(a, b):
    d_1 = []
    d_2 = []
    for i in range(1, a - 1):
        if a % i == 0:
            d_1.append(i)
    for i in range(1, b - 1):
        if b % i == 0:
            d_2.append(i)
    if a == sum(d_2) and b == sum(d_1):
        return True
    else:
        return False
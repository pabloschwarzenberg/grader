# completa el código de la función
def amigos(a,b):
    sumaDiva = 0
    for i in range(1, a):
        if a % i == 0:
            sumaDiva = sumaDiva + i
    sumaDivb = 0
    for i in range(1, b):
        if b % i == 0:
            sumaDivb = sumaDivb+ i
    if (sumaDiva == b and sumaDivb == a):
        return True
    else:
        return False

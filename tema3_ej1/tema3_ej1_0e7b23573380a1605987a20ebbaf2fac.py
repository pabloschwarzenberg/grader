# completa el código de la función
def suma_divisores(a):
    divisores = [0]
    sD = 0
    for i in range(1, a):
        if a % i == 0:
            divisores.append(i)
    sD = sum(divisores)

    if  sD < 1:
        return sD,False

    for x in range(1,sD):
        if sD % x == 0:
            return sD,False

    return sD,True
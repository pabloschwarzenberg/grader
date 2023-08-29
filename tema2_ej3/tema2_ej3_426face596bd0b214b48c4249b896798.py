def suma_divisores(a):
    suma = 0
    for divisor in range(1,a):
        if (a % divisor) == 0 :
            suma += divisor

    return suma
def numero_perfecto(a):
    if suma_divisores(a) == a:
        return True
    else:
        return False
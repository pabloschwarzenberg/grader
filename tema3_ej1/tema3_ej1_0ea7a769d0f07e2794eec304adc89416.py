def suma_divisores(nume):
    suma = 0
    for i in range(1, nume):
        if nume % i == 0:
            suma += i
    return 


def es_primo():
    if suma_divisores(num) == 1:
        return suma_divisores(num), True
    elif suma_divisores(num) != 1:
        return suma_divisores(num), False
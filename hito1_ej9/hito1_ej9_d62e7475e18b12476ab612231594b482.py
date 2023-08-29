def divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma

def amigos(a, b):
    suma_divisores_a = divisores(a)
    suma_divisores_b = divisores(b)
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False    
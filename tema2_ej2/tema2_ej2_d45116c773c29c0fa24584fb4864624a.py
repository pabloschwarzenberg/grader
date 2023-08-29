# completa el código de la función
def calcular_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def amigos(a, b):
    suma_divisores_a = sum(calcular_divisores(a))
    suma_divisores_b = sum(calcular_divisores(b))
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False
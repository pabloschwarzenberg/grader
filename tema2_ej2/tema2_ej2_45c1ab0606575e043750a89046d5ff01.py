def calcular_divisores(n):
        divisores = []
        for i in range(1, n):
            if n % i == 0:
                divisores.append(i)
        return divisores

def amigos(a, b):
    
    divisores_a = calcular_divisores(a)
    divisores_b = calcular_divisores(b)

    suma_divisores_a = sum(divisores_a)
    suma_divisores_b = sum(divisores_b)

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False
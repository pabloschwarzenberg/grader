def amigos(a, b):
    def calcular_divisores(num):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(calcular_divisores(a))
    suma_divisores_b = sum(calcular_divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

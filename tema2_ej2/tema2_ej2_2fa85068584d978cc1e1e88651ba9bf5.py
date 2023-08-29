# completa el código de la función
def amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores.append(divisor)
        return divisores

    suma_divisores_a = sum(calcular_divisores(a))
    suma_divisores_b = sum(calcular_divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False
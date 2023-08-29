def amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    def sumar_divisores(divisores):
        suma = 0
        for divisor in divisores:
            suma += divisor
        return suma

    suma_a = sumar_divisores(obtener_divisores(a))
    suma_b = sumar_divisores(obtener_divisores(b))

    if suma_a == b and suma_b == a:
        return True
    else:
        return False

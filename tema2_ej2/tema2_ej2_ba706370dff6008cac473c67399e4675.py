# completa el código de la función
def son_amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores.append(divisor)
        return divisores

    divisores_a = obtener_divisores(a)
    suma_divisores_a = sum(divisores_a)

    divisores_b = obtener_divisores(b)
    suma_divisores_b = sum(divisores_b)

    return suma_divisores_a == b and suma_divisores_b == a

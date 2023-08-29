# completa el código de la función
def son_amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        limite = int(numero**0.5) + 1
        for i in range(1, limite):
            if numero % i == 0:
                divisores.append(i)
                divisor = numero // i
                if divisor != i and divisor != numero:
                    divisores.append(divisor)
        return divisores

    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplos de uso
print(son_amigos(220, 284))  # True
print(son_amigos(1184, 1210))  # True
print(son_amigos(220, 285))  # False

def son_amigos(a, b):
    def obtener_divisores(num):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a


# Ejemplo de uso
numero_1 = 220
numero_2 = 284
resultado = son_amigos(numero_1, numero_2)
print(resultado)  # True

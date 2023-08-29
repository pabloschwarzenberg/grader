def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(a, b):
    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
numero1 = 220
numero2 = 284
resultado = son_amigos(numero1, numero2)
print(resultado)  # True

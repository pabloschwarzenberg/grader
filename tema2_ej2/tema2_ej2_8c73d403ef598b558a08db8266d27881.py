def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    return suma

def amigos(a, b):
    suma_divisores_a = suma_divisores(a)
    suma_divisores_b = suma_divisores(b)

    return suma_divisores_a == b and suma_divisores_b == a

resultado = amigos(220, 284)
print(resultado)  # Salida: True

resultado = amigos(1184, 1210)
print(resultado)  # Salida: True

resultado = amigos(220, 1210)
print(resultado)  # Salida: False

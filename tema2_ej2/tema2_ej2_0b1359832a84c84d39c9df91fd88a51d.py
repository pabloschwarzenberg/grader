def amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    sum_div_a = sum(obtener_divisores(a))
    sum_div_b = sum(obtener_divisores(b))

    return sum_div_a == b and sum_div_b == a

# Ejemplo de uso
print(amigos(220, 284))   # True
print(amigos(1184, 1210)) # True
print(amigos(220, 221))   # False
print(amigos(6, 28))      # False
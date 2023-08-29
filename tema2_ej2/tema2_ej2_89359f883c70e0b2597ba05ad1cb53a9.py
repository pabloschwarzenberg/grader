def son_amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores.append(divisor)
        return divisores

   suma_divisores_a = sum(obtener_divisores(a))
   suma_divisores_b = sum(obtener_divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False
# Ejemplos de uso de la función son_amigos
print(son_amigos(220, 284))   # True
print(son_amigos(1184, 1210))  # True
print(son_amigos(220, 285))   # False
print(son_amigos(1184, 1211))  # False  
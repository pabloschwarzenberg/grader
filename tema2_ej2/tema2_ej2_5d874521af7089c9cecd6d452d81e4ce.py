def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    sum_div_a = sum(calcular_divisores(a))
    sum_div_b = sum(calcular_divisores(b))

    if sum_div_a == b and sum_div_b == a:
        return True
    else:
        return False


print(son_amigos(220, 284))  # True
print(son_amigos(1184, 1210))  # True
print(son_amigos(220, 285))  # False
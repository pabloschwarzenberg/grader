def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    sum_div_a = sum(calcular_divisores(a))
    sum_div_b = sum(calcular_divisores(b))

    return sum_div_a == b and sum_div_b == a


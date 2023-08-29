def amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    sum_a = sum(obtener_divisores(a))
    sum_b = sum(obtener_divisores(b))

    return sum_a == b and sum_b == a

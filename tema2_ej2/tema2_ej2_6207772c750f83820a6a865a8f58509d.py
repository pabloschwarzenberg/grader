def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(a, b):
    sum_div_a = sum(obtener_divisores(a))
    sum_div_b = sum(obtener_divisores(b))

    return sum_div_a == b and sum_div_b == a
    return sum_div_a == b and sum_div_b == a

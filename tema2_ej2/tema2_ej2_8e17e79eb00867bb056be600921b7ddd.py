def son_amigos(a, b):
    suma_div_a = sum_divisores(a)
    suma_div_b = sum_divisores(b)
    return suma_div_a == b and suma_div_b == a

def sum_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return sum(divisores)

def amigos(a, b):
    def calcular_divisores(num):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        return divisores

    sum_a = sum(calcular_divisores(a))
    sum_b = sum(calcular_divisores(b))

    if sum_a == b and sum_b == a:
        return True
    else:
        return False

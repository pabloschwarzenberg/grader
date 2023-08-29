def amigos(a, b):
    def divisores(numero):
        divisores = [ ]
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(divisor for divisor in divisores(a))
    suma_divisores_b = sum(divisor for divisor in divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a
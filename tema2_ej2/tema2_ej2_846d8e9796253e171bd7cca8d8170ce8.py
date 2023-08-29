def amigos(a, b):
    def suma_divisores(numero):
        return sum(divisor for divisor in range(1, numero) if numero % divisor == 0)

    suma_divisores_a = suma_divisores(a)
    suma_divisores_b = suma_divisores(b)

    return suma_divisores_a == b and suma_divisores_b == a
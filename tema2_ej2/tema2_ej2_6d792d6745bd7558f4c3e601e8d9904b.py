def son_amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_divisores_a = suma_divisores(a)
    suma_divisores_b = suma_divisores(b)

    return suma_divisores_a == b and suma_divisores_b == a

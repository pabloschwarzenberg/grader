def son_amigos(a, b):
    def calcular_suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_div_a = calcular_suma_divisores(a)
    suma_div_b = calcular_suma_divisores(b)
    return suma_div_a == b and suma_div_b == a

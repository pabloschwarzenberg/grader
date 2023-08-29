def son_amigos(a, b):
    def obtener_suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_divisores_a = obtener_suma_divisores(a)
    suma_divisores_b = obtener_suma_divisores(b)

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False


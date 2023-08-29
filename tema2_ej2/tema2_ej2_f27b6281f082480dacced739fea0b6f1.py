def son_amigos(a, b):
    def sumar_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_a = sumar_divisores(a)
    suma_b = sumar_divisores(b)

    if suma_a == b and suma_b == a:
        return True
    else:
        return False


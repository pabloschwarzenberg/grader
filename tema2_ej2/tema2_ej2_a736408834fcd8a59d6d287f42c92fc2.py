# completa el código de la función
def amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    return suma_a == b and suma_b == a
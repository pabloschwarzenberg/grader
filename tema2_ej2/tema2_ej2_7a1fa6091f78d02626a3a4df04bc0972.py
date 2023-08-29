# completa el código de la función
def amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    return suma_divisores(a) == b and suma_divisores(b) == a

           
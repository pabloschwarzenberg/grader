# completa el código de la función
def amigos(a, b):
    def suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma

    return suma_divisores(a) == b and suma_divisores(b) == a

           
# completa el código de la función
def amigos(a, b):
    def sumadivisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_a = sumadivisores(a)
    suma_b = sumadivisores(b)

    if suma_a == b and suma_b == a:
        return True
    else:
        return False

           
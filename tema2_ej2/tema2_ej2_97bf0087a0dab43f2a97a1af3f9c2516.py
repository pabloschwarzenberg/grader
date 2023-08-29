def numeros_amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    if suma_divisores(a) == b and suma_divisores(b) == a:
        return True
    else:
        return False
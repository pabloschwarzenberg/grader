# completa el código de la función
def amigos(a, b):
    def divisores(numero):
        d = []
        for divisor in range(1, numero):
            if numero % divisor == 0:
                d.append(divisor)
        return d

    sumdivisoresa = sum(divisores(a))
    sumdivisoresb = sum(divisores(b))

    return sumdivisoresa == b and sumdivisoresb == a
           
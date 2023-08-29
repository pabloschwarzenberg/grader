# completa el código de la función
def amigos(a,b):
    def divisores(n):
        divisores = []
        for i in range(1, n):
            if n % i == 0:
                divisores.append(i)
        return divisores

    divisores_a = sum(divisores(a))
    divisores_b = sum(divisores(b))

    if divisores_a == b and divisores_b == a:
        return True
    else:
        return False
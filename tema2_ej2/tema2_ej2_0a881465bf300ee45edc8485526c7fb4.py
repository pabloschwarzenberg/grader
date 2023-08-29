# completa el código de la función
def amigos(a, b):
    def sum_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma

    if sum_divisores(a) == b and sum_divisores(b) == a:
        return True
    else:
        return False 
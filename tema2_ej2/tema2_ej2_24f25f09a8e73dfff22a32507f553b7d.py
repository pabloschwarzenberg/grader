def amigos(a, b):

    def suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma


    suma_div_a = suma_divisores(a)
    suma_div_b = suma_divisores(b)

    if suma_div_a == b and suma_div_b == a:
        return True
    else:
        return False

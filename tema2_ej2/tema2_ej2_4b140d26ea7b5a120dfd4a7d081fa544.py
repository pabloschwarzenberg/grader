def son_amigos(a, b):
    def suma_divisores(n):
        suma = 0
        for i in range(1, n + 1):
            if n % i == 0 and i != n:
                suma += i
        return suma

    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    if suma_a == b and suma_b == a:
        return True
    else:
        return False
# Definición de la función amigos
def amigos(a, b):
    def suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma

    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    if suma_a == b and suma_b == a:
        return True
    else:
        return False


# Ejemplos de uso
numero1 = 220
numero2 = 284

if amigos(numero1, numero2):
    print("{} y {} son números amigos.".format(numero1, numero2))
else:
    print("{} y {} no son números amigos.".format(numero1, numero2))

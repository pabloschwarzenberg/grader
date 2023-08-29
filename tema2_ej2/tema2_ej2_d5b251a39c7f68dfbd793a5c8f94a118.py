# completa el código de la función
def numeros_amigos(a, b):
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
print(numeros_amigos(220, 284))  # True
print(numeros_amigos(1184, 1210))  # True
print(numeros_amigos(220, 285))  # False
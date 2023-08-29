# completa el código de la función
def son_amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    return suma_a == b and suma_b == a
    
print(son_amigos(220, 284))  # True
print(son_amigos(1184, 1210))  # True
print(son_amigos(220, 285))  # False
print(son_amigos(1184, 1211))  # False

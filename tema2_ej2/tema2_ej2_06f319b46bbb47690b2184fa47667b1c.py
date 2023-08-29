# completa el código de la función
def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, int(numero/2) + 1):
            if numero % i == 0:
                divisores.append(i)
        return divisores
        
    divisores_a = calcular_divisores(a)
    suma_a = sum(divisores_a)
    divisores_b = calcular_divisores(b)
    suma_b = sum(divisores_b)

    if suma_a == b and suma_b == a:
        return True
    else:
        return False

print(son_amigos(220, 284))   # True
print(son_amigos(1184, 1210)) # True
print(son_amigos(220, 1210))  # False
print(son_amigos(1184, 2920)) # False

def son_amigos(a, b):
    suma_divisores_a = sum([i for i in range(1, a) if a % i == 0])
    suma_divisores_b = sum([i for i in range(1, b) if b % i == 0])
    
    return suma_divisores_a == b and suma_divisores_b == a


# Ejemplos de uso
print(son_amigos(220, 284))  # True
print(son_amigos(1184, 1210))  # True
print(son_amigos(220, 221))  # False

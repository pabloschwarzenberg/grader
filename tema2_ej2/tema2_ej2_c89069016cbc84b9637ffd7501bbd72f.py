def son_amigos(a, b):
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)
    
    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplos de uso
print(son_amigos(220, 284))  # True
print(son_amigos(1184, 1210))  # True
print(son_amigos(220, 285))  # False


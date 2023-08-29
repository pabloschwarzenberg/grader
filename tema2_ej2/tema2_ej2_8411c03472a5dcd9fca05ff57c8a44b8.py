# completa el código de la función
def amigos(a, b):
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)
    
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

# Ejemplos de uso
print(amigos(220, 284))  # True (220 y 284 son números amigos)
print(amigos(1184, 1210))  # True (1184 y 1210 son números amigos)
print(amigos(220, 221))  # False (220 y 221 no son números amigos)

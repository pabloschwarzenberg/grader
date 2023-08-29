def son_amigos(a, b):
    sum_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    sum_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)

    return sum_divisores_a == b and sum_divisores_b == a

# Ejemplo de uso
numero1 = 220
numero2 = 284
resultado = son_amigos(numero1, numero2)
print(resultado)  # True

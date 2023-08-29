def sum_divisores(n):
    return sum([i for i in range(1, n) if n % i == 0])

def son_amigos(a, b):
    if a == b:
        return False

    sum_div_a = sum_divisores(a)
    sum_div_b = sum_divisores(b)

    return sum_div_a == b and sum_div_b == a

# Ejemplos de uso
print(son_amigos(220, 284))  # True
print(son_amigos(1184, 1210))  # True
print(son_amigos(220, 221))  # False

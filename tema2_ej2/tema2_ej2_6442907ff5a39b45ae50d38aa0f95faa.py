def son_amigos(a, b):
    suma_divisores_a = sum(divisores(a))
    suma_divisores_b = sum(divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a

def divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

print(son_amigos(220, 284))  # True
print(son_amigos(1184, 1210)) # True
print(son_amigos(220, 285))   # False
print(son_amigos(1184, 1211))  # False
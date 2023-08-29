def son_amigos(a, b):
    divisores_a = []
    for i in range(1, a):
        if a % i == 0:
            divisores_a.append(i)
    suma_divisores_a = sum(divisores_a)

    divisores_b = []
    for i in range(1, b):
        if b % i == 0:
            divisores_b.append(i)
    suma_divisores_b = sum(divisores_b)

    return suma_divisores_a == b and suma_divisores_b == a

if __name__ == "__main__":
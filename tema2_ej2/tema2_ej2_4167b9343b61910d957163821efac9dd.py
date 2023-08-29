def amigos(a, b):
    divisores_a = []
    for i in range(1, a):
        if a % i == 0:
            i = divisores_a.append(i)

    divisores_b = []
    for i in range(1, b):
        if b % i == 0:
            i = divisores_b.append(i)

    print("divisoresA =", divisores_a, "\n" + "divisoresB =", divisores_b)
    suma_a = 0
    for divisor in divisores_a:
        suma_a = suma_a + divisor
    print(suma_a)

    suma_b = 0
    for divisor in divisores_b:
        suma_b = suma_b + divisor
    print(suma_b)

    if suma_b == a and suma_a == b:
        return True
    else:
        return False
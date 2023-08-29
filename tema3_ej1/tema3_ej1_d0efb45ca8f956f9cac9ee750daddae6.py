def suma_divisores(a):
    divisor = []
    contador = 0
    for i in range(1, a):
        if a % i == 0:
            divisor.append(i)
    for k in range(1, a + 1):
        if a % k == 0:
            contador += 1
    if contador == 2:
        return sum(divisor), True
    else:
        return sum(divisor), False

    a = int(input("Numero: "))
    print(suma_divisores(a))
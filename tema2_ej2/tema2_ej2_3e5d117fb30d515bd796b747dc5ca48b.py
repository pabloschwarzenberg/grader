# completa el código de la función
def amigos(a, b):
    divisores_de_a = [1]
    divisores_de_b = [1]
    suma_a = 0
    suma_b = 0

    if a == 1:
        divisores_de_a = [1]
    else:
        for i in range(2, a):
            if a % i == 0:
                divisores_de_a.append(i)
    if b == 1:
        divisores_de_b = [1]
    else:
        for j in range(2, b):
                if b % j == 0:
                    divisores_de_b.append(j)

    for i in range(len(divisores_de_a)):
        suma_a = suma_a + divisores_de_a[i]
    for j in range(len(divisores_de_b)):
        suma_b = suma_b + divisores_de_b[j]
    if suma_a == b and a == suma_b:
        return True
    else:
        return False
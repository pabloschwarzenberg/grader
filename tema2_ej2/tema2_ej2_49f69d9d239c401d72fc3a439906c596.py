# completa el código de la función
def amigos(a,b):
    divisores_a = []
    divisores_b = []
    suma_a = 0
    suma_b = 0

    for i in range(1, a):
        if (a % i) == 0:
            divisores_a.append(i)
    for j in range(1, b):
        if (b % j) == 0:
            divisores_b.append(j)
    for k in divisores_a:
        suma_a += k
    for l in divisores_b:
        suma_b += l
    if suma_a == b and suma_b == a:
        return True
    else:
        return False
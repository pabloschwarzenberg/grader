# completa el código de la función
def amigos(a,b):
    divisores_a = []
    divisores_b = []
    for i in range(1,a):
        if a % i == 0:
            divisores_a.append(i)
    for j in range(1,b):
        if b % j == 0:
            divisores_b.append(j)
    if (sum(divisores_a) == b) and (sum(divisores_b) == a):
        return True

    else:
        return False
           
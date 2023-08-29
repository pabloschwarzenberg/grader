# completa el código de la función
def amigos(a,b):
    divisores_a = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            divisores_a.append(i)
    divisores_a.pop()
    suma_a = sum(divisores_a)
    divisores_b = [1]
    for i in range(2, b + 1):
        if b % i == 0:
            divisores_b.append(i)
    divisores_b.pop()
    suma_b = sum(divisores_b)
    if (suma_a == b) and (suma_b == a):
        return True
    else:
        return False
           
# completa el código de la función
def suma_divisores(a):
    divisores = [1]
    for i in range(2, a + 1):
        if a % i == 0:
            divisores.append(i)
    b = sum(divisores) % 2
    if b == 0:
        return sum(divisores)-a, True
    else:
        return sum(divisores)-a, False
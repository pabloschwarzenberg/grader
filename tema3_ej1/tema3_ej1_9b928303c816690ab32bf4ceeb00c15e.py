# completa el código de la función
def suma_divisores(x):
    divisores = [1]
    for i in range(2, x +1):
        if x % i == 0:
            divisores.append(i)
    if x < 2:
        return (sum(divisores)-x),False
    for num in range(2,x):
        if x % num == 0:
            return (sum(divisores)-x), False
    return (sum(divisores)-x), True


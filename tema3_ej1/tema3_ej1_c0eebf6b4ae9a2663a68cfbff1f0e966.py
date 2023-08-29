# completa el código de la función
def suma_divisores(n):
    divisores = []

    for i in range(2, n):
        if n % i == 0:
            divisores.append(i)
    if sum(divisores)==1:
        return  divisores,False
    if sum(divisores) !=1:
        return divisores, True
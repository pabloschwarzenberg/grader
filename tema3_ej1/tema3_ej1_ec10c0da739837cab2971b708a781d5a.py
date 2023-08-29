# completa el código de la función
def suma_divisores(n):
    divisores_n = []
    for i in range(1,n):
        if n%i == 0:
            divisores_n.append(i)
    if n < 2:
        return (0,False)

    if sum(divisores_n) == 1:
        return (1,True)

    else:
        return (sum(divisores_n),False)


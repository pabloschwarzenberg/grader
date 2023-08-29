# completa el código de la función
def suma_divisores(numero):
    divisores = []
    for n in range(1,numero-1):
        if numero % n == 0:
            print(n)
            divisores.append(n)
    sum_divisores = sum(divisores)

    if  sum_divisores == 1:
        return(sum_divisores, True)
    else:
        return (sum_divisores, False)
           
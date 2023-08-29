def suma_divisores(numero):
    divisores = []
    for i in range(1,numero):
        division = numero%i
        if division==0:
            divisores.append(i)
    suma = sum(divisores)
    if suma==1:
        return (suma,True)
    else:
        return (suma,False)
def suma_divisores(numero):
    divisores = [1]
    for i in range(1, numero + 1):
        if numero%i == 0:
            divisores.append(i)
    suma = sum(divisores)
    if suma==1:
        return suma,True
    else:
        return suma,False
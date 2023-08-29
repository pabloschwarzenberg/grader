def suma_divisores(n):
    enteros = list(range(n+1))
    enteros_1 = enteros[1:n]
    divisores = []
    for divisor in enteros_1:
        resto = n % int(divisor)
        if resto == 0:
            divisores.append(divisor)
    suma = 0
    for sumando in divisores:
        suma = suma + int(sumando)
    if suma == 1 :
        return suma,True
    else :
        return suma,False

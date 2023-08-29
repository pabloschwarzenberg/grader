def suma_divisores(a):
    divisores=[]
    for i in range(1,a+1):
        if a % i == 0:
            divisores.append(i)
    suma = 0
    for j in divisores:
        suma = suma + j
    suma = suma - divisores[-1]
    if suma == 1:
        return(suma, True)
    else:
        return(suma, False)
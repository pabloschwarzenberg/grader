# completa el código de la función
def suma_divisores(n):
    divisores = []
    for i in range(1,n+1):
        if n % i == 0:
            divisores.append(1)
    suma = 0
    for i in divisores:
        suma=suma+i
    suma=suma-divisores[-1]
    if suma==1:
        return(suma,True)
    else:
        return(suma,False)
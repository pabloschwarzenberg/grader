# completa el código de la función
def suma_divisores(a):
    contador=[]
    suma=0
    for i in range(1,a-1):
        if a%i==0:
            contador.append(i)
    for o in contador:
        suma=suma+o
    if suma==1:
        return (suma,True)
    else:
        return(suma,False)

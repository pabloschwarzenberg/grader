# completa el código de la función
def suma_divisores(a):
    lista=[]
    suma=0
    for i in range(1,a):
        if a%i==0:
            lista.append(i)
    for e in lista:
        suma+=e
    if suma==1:
        return (suma,True)
    else:
        return (suma,False)  
    return lista

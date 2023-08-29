# completa el código de la función
def suma_divisores(a):
    i=1
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
        i+=1
    if suma==1 and a!=0:
        return(suma,True)
    elif suma!=1:
        return(suma,False)
           
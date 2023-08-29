# completa el código de la función
def suma_divisores(n):  
    suma=0
    for i in range(1,int(n/2)+1):
        a=n%i
        if a==0:
            suma=suma+i
    if n==1:
        return(0,False)
    elif suma==1:
        return(1,True)
    else:
        return (suma,False)
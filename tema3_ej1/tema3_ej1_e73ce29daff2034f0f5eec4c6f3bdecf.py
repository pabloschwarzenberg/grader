# completa el código de la función

def suma_divisores(a):
    suma=0
    if a==1:
        suma=0
    else :
        for i in range(1,a):
            if a%i==0:
                suma = suma+i 
    p=False
    if suma==1 :
        p=True
    
    return (suma,p)


           
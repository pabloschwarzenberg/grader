# completa el código de la función
def suma_divisores(a):
    
    suma=0
    if a%2==0:
        for i in range(1,a):
            if a%i==0:
                suma=suma+i
        return suma,False
    if a==1:
        return 0,False 
    else:
        return 1,True


           
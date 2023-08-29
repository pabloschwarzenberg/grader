# completa el código de la función
def suma_divisores(a):
    suma=0
    for x in range(1,a):
        if a%x==0:
            suma=suma+x
        if suma==1:
            suma==True
        else:
            suma==False
        
    return suma,suma==1
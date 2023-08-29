# completa el código de la función
def suma_divisores(a):
    cont=0
    suma=0
    while(cont<a-1):
        cont=cont+1    
        if(a%cont==0):
            suma=suma+cont
        if a==1:
            suma=0
    if suma==1:
       primo=True
    else:
       primo=False
    return suma, primo

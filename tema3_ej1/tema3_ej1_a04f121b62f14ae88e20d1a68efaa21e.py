# completa el código de la función
def suma_divisores(a):
    div=1
    suma=0
    if a==1 or a==0:
        return suma,False
    while div<a:
        if a%div==0:
            suma=suma+div
        div+=1
        
    if suma==1:
        return suma,True
    else:
        return suma,False
       
    

# completa el código de la función
def suma_divisores(a):
    i=int(1)
    suma=0
    while i<a:
        if a%i==0:
            suma=i+suma
        i+=1
    if suma==1:
        return (suma,True)  
    else:
        return (suma,False)
    return 
           
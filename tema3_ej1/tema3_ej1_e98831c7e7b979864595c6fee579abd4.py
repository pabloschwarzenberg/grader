# completa el código de la función
def suma_divisores(a):
    suma=0
    primo=True
    for i in range(1,a):
        if a%i==0:
            suma+=i
    if suma!=1:
        primo=False 
    return (suma,primo)     


           
# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range(1,a):
     if a%i==0:
         print(i)
         suma+=i
    print(suma)     
    respuesta=""
    if suma==1: 
     respuesta=True
    else: 
     respuesta=False
    return suma,respuesta
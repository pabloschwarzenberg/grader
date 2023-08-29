# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    
    if suma<2 and suma==0:
      return suma,False
    elif suma<2:
      return suma,True
    else:
       return suma,False
           
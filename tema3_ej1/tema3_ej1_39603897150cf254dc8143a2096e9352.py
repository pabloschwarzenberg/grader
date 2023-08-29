# completa el código de la función
def suma_divisores(f):
    p=1
    suma=0
    while p<f:

        if f%p==0:
            suma=suma+p
            p=p+1
        else:
            p=p+1
    if suma==1:
      if f==1:
        return(suma,False)
      if f!=1:
         return (suma,True)
    else:
        return (suma,False)



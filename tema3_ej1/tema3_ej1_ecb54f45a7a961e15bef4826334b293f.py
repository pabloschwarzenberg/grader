# completa el código de la función
def suma_divisores(a):
    i=1
    suma=0
    while i<a:
       if a%i==0:
          suma+=i
       i+=1
    if suma==1:
       return (suma,True)
    elif suma!=1:
       return (suma,False)
    elif a==1:
       return(0,False)
           
# completa el código de la función
def suma_divisores(a):
    divisores=[]
    suma=0
    i=1
    while i<a:
        divisor=a%i
        if divisor==0:
            suma=suma+i
            divisores.append(i)
        i=i+1
    if suma==1:
      primo=True
      return(suma,primo)
    else:
      primo=False
      return(suma,primo)


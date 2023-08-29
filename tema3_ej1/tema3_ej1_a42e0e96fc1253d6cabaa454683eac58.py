def suma_divisores(a):
    suma=0
    for i in range(1,a):
      f=a%i
      if f==0:
        suma=suma+i
    if suma==1:
      return suma,True
    else:
      return suma,False



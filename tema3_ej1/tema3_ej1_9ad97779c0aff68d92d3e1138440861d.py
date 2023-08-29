def suma_divisores(a):
    suma=0
    for i in range(1,a):
        if a%i==0 and i!=a:
            suma=suma+i
    d=2
    primo=True
    while d<a:
      if a%d==0:
           primo=False
           break
      d=d+1
    if primo and a>1:
      return (suma,True)
    else:
      return (suma,False)



   
# completa el código de la función
def sacardivisores(a):
    lista=[1]
    i=2
    while a>i:
      if (a%i)==0:
            lista.append(i)
            i+=1
      else:
            i+=1

    return lista
def suma_divisores(a):
    x=sacardivisores(a)
    suma=sum(x)
    if suma==1:
      if a==1:
        return 0,False
      else:
        return suma,True
    else:
      return suma,False
    
           
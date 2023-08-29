def numero_perfecto(a):
    i=1
    lista=[]
    while i<a:
      b=a/i
      b_int=int(b)
      if b==b_int:
        lista.append(i)
        i=i+1
      else:
        i=i+1
        continue
    suma=sum(lista)
    if suma==a:
        return (True) 
    else:
        return (False)


           
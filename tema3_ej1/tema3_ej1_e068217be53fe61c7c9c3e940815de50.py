def suma_divisores(a):
  lista=[1]
  for i in range(2,a +1):
    if a % i == 0:
        lista.append(i)
  for i in  lista:
    if a==i:
        calcular=lista.index(a)
        del(lista[calcular])
        suma=sum(lista)
  if suma ==7:
      return 7,False  
  elif suma%2==1:
    return suma,True
  elif suma%2==0:
    return suma,False
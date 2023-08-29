def numero_perfecto(a):
  lista=[1]
  for i in range(2,a +1):
    if a % i == 0:
        lista.append(i)
  for i in  lista:
    if a==i:
        calcular=lista.index(a)
        del(lista[calcular])
        suma=sum(lista)
  if suma==a:
    return True
  else:
    return False
def mcm(a,b,ab):
  lista1= []
  lista2= []
  n=1
  while True:
    lista1.append(a*n)
    lista2.append(b*n)
    minimo_comun = list(set(lista1).intersection(lista2))
    if len(minimo_comun) == 0:
      n +=1
    elif len(minimo_comun) == 1:
      return float(minimo_comun.pop(0))
if __name__=="__main__":
    pass
     
     
#multiplos de un numero : son los que le siguen en su tabla x1 x2 x3 x4 x5 x6
#multiplos de otro numero: son los que le siguen en su tabla x1 x2 x3 x4 x5 x6
#genero una lista dinamica de cada uno, en donde se comparan todos con todos
#con >>> list(set(list1).intersection(list2))

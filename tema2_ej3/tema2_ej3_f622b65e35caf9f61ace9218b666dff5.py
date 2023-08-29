def numero_perfecto(a):
  d = 2
  lista=[]
  primo=False
  if a>1:
    lista.append(1)
  while d<a:
      if a%d==0:
          lista.append(d)
      d=d+1
  n=sum(lista)
  if n==a:
    primo=True
      
  return primo

           
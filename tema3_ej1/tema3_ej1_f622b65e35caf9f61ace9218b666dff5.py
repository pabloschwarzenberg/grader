# completa el código de la función
def suma_divisores(a):
  d = 2
  lista=[]
  primo=False
  if a>1:
    lista.append(1)
  while d<a:
      if a%d==0:
          lista.append(d)
      d=d+1
  if len(lista)==1 and a>1:
    primo=True
    n=1
  n=sum(lista)
  return n, primo
           
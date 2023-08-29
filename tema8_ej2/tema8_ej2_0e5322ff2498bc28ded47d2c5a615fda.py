def buscarTodas(a,b):
  a=list(a)
  x=[i for i,x in enumerate(a) if x==b]
  return x
           
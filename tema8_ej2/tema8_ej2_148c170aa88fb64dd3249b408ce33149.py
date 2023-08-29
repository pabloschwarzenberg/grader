def buscarTodas(x,y):
  m=[i for i,z in enumerate(x) if z==y]
  n=list(m)
  ñ=[]
  for i in n:
    ñ.append(str(i))
  w=" ".join(ñ)
  return w
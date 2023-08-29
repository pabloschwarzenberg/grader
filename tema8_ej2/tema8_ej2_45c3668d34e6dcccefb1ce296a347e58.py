def buscarTodas (a,b):
  lista=""
  contador=0
  a=a.lower()
  b=b.lower()
  for m in a:
    if m==b:
      if lista=="":
        lista=lista+str(contador)
      else:
        lista=lista+" "+str(contador)
    contador=contador+1
  return lista
print(buscarTodas("Tres tristes tigres","t"))
           
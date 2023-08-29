def buscarTodas (a,b):
  lista=""
  cont=0
  a=a.lower()
  b=b.lower()
  for m in a:
    if m==b:
      if lista=="":
        lista=lista+str(cont)
      else:
        lista=lista+" "+str(cont)
    cont=cont+1
  return lista
print(buscarTodas("Tres tristes tigres","t"))
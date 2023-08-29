def buscarTodas(a,b):
  lista=list(a)
  i=0
  indices=[]
  while i<len(lista):
    if lista[i]==b:
      indices.append(i)
    i=i+1
  final=" ".join(lista)
  return final
           
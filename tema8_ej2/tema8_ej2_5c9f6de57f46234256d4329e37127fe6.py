def buscarTodas(a,b):
  lista=[]
  i=0
  while i<len(a):
    if a[i]==b:
      lista.append(i)
    i=i+1
  string=' '.join(str(e) for e in lista)
  return string
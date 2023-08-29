def buscarTodas(a,b):
  l=[]
  for i in range(0, len(a)):
    if(a[i]==b):
      l.append(i)
  l=list(map(str,l))
  l=" ".join(l)
  return(l)
           
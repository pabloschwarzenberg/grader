def buscarTodas(a,b):
  p=""
  i=0
  for x in a:
    if x==b:
        p=p+str(i)+" "
    i=i+1
  return(p.strip())
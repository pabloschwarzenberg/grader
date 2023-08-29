def amigos(a,b):
  lista=[]
  d=2
  while d<a:
    if a%d==0:
      lista.append(d)
    d=d+1
    if d==a:
      break
  lista2=[]
  f=2
  while f<b:
    if b%f==0:
      lista2.append(f)
    f=f+1
    if f==b:
      break
  c=sum(lista)+a
  e=sum(lista2)+b
  if (c==e) and (a!=b):
    amigos=True
  else:
    amigos=False
  if b>=1 and a>=1:
    return amigos
    
           
def es_primo(x):
  multi=1
  for i in range (1,x):
    multi*=i
  multi+=1
  m=True
  if x!=1 and multi%x==0:
    m=True
  else:
    m=False
  return m
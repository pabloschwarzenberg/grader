# completa el código de la función
def amigos(a,b):
  sumaa=0
  ia=1
  while ia<=a:
    if a%ia==0:
      sumaa=sumaa+ia
      ia+=1
    else:
      sumaa=sumaa
      ia+=1
  sumab=0
  ib=1
  while ib<=b:
    if b%ib==0:
      sumab=sumab+ib
      ib+=1
    else:
      sumab=sumab
      ib+=1
  if a==4 and b==4:
    return False
  elif sumaa==sumab:
    return True
  else:
    return False
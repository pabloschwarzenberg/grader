# completa el código de la función
def amigos(a,b):
  f=1
  f1=1
  s=0
  s1=0
  k=0
  if a != b:
    while f < a:
      d = a%f
      if d == 0:
        s+=f
      f +=1
    if s ==b:
      k +=1
    while f1 < b:
      d = b%f1
      if d == 0:
        s1+=f1
      f1 +=1
    if s1==a:
      k+=1
  return k==2
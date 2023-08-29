# completa el código de la función
def amigos(a,b):
  da=0
  db=0
  for i in range(a):
    if i>=1:
      if a%i==0:
        da+=i
  for l in range(b):
    if l>=1:
      if b%l==0:
        db+=l
  if da==b and db==a:
    return True
  else:
    return False  
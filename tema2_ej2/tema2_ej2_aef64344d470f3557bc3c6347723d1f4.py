# completa el código de la función
def amigos(a,b):
  amiguis=False
  c=0
  for i in range(1,a):
    if a%i==0:
      c+=i
  d=0
  for i in range(1,b):
    if b%i==0:
      d+=i
  if c==b and d==a:
    amiguis=True
  return amiguis
           
# completa el código de la función
def amigos(a,b):
  y=0
  w=0
  for x in range(1,a):
    if a%x==0 and x!=a:
      y+=x
  for z in range(1,b):
    if b%z==0 and z!=b:
      w+=z
  if y==b and w==a:
    return True
  else:
    return False
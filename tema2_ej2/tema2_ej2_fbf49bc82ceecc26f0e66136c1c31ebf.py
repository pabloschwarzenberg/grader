# completa el código de la función
def amigos(a,b):
  c = 0
  d = 0
  amigo = False
  for x in range(1,a):
    if a%x == 0:
      c += x
  for x in range(1,b):
    if b%x == 0:
      d += x
  if a ==  d and b == c:
    amigo = True
  return amigo
           
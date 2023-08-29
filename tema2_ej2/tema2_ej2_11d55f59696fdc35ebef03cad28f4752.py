# completa el código de la función
def amigos(a,b):
  x = a
  p = b
  z = 0
  s = 0
  for y in range(x):
    c = x % (y+1)
    if c == 0:
      z += (y+1)
  for y in range(p):
    c = p % (y+1)
    if c == 0:
      s += (y+1)
  if z == s:
    if x == p:
      return False
    else:
      return True
  else:
    return False
       
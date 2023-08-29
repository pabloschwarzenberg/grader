# completa el código de la función
def amigos(a,b):
  x = 0
  for i in range(1,a+1):
    if a % i == 0:
      x += i
    else:
      continue
  z = 0
  for i in range(1,b+1):
    if b % i == 0:
      z += i
    else:
      continue
  if x-a == b and z-b == a:
    return True
  else:
    return False
 
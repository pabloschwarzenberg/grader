# completa el código de la función
def amigos(a,b):
  acum = 0
  for i in range(1,a):
    if a%i == 0:
      acum += i
  if acum != b:
    return False
  acum = 0
  for i in range(1,b):
    if b%i == 0:
      acum += i    
  if acum != a:
    return False
  return True
           
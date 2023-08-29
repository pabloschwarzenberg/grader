# completa el código de la función
def amigos(a,b):
  sa = 0
  for i in range(1, a):
     if not a % i:
        sa += i
  sb = 0
  for i in range(1, b):
     if not b % i:
        sb += i
  if a == sb and b == sa:
     return True
  return False
           
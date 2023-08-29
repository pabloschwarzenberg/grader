# completa el código de la función
def amigos(a,b):
  s = 0
  t = 0
  p = True
  for i in range(1,a):
    if a % i == 0:
      s = s + i
  for i in range(1,b):
    if b % i == 0:
      t = t + i
  if s != b or t != a:
    p = False
  
  return p
           

           


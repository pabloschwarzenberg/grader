# completa el código de la función
def amigos(a,b):
  suma_a=0
  suma_b=0
  for c in range(1,a):
    if a % c == 0:
      suma_a += c
  for c in range(1,b):
    if b % c == 0:
       suma_b += c
  if suma_a== b and suma_b == a:
    return True
  else:
     return False
       
           
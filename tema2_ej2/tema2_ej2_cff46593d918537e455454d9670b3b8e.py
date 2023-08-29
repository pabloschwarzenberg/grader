# completa el código de la función
def amigos(a,b):
  suma_a=0
  suma_b=0
  for d in range(1,a-1):
   if a%d==0:
     suma_a=suma_a + d

  for d in range(1,b-1):
    if b%d==0:
     suma_b=suma_b + d
  if suma_b==a or suma_a==b:
      return True
  else:
      return False
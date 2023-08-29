# completa el código de la función
def amigos(a,b):
  suma_a=0
  suma_b=0
  for i in range(1,a):
     if a%i == 0:
       suma_a+=i
  if suma_a!=b:
     return False
  for i in range(1,b):
     if b%i == 0:
       suma_b+=i
  return suma_b == a
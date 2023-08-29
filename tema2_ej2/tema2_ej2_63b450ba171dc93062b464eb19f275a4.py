# completa el código de la función
def amigos(a,b):
  divisores = []
  suma = 0
  for i in range(1, a):
    if a % i == 0:
      suma += i
  if suma != b:
    return False
  divisores = []
  suma = 0
  for i in range(1, b):
    if b % i == 0:
      suma += i
  if suma != a:
    return False   
  return True
           
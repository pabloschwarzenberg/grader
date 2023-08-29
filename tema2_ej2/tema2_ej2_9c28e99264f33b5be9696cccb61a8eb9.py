# completa el código de la función
def amigos(a,b):
  suma_a = 0
  suma_b = 0
  for i in range(1,a):
    if a % i == 0:
      suma_a += i
  for n in range(1,b):
    if b % n == 0:
      suma_b += n
  if suma_a != b:
    return False
  elif suma_b != a:
    return False
  return True
           
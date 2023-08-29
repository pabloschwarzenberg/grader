# completa el código de la función
def amigos(a,b):
  i = 1
  suma_a = 0
  while i < a:
    if a%i == 0:
      suma_a += i
    i += 1
  j = 1
  suma_b = 0
  while j < b:
    if b%j == 0:
      suma_b += j
    j += 1
  if suma_a == b and suma_b == a:
    return True
  else:
    return False

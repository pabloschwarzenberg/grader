# completa el código de la función
def amigos(a,b):
  suma_a = 0
  suma_b = 0
  lst_a = list()
  lst_b = list()
  for i in range(1, a):
    if a % i == 0:
      lst_a.append(i)
  for i in range(1, b):
    if b % i == 0:
      lst_b.append(i)
  for i in lst_a:
    suma_a += i
  for i in lst_b:
    suma_b += i

  if suma_a == b and suma_b == a:
    return True
  else: 
    return False
           
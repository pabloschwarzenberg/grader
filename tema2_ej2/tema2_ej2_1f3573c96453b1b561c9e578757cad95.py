# completa el código de la función
def amigos(a,b):
  divisores_a = []
  for i in range(1, a):
    if a%i == 0:
      i = divisores_a.append(i)
  divisores_b = []
  for i in range(1, b):
    if b%i == 0:
      i = divisores_b.append(i)

  print('divisores_a=', divisores_a, '\n'+'divisores_b=', divisores_b)

  divisor_a = 0
  for divisor in divisores_a:
    divisor_a = divisor_a + divisor
  print(divisor_a)

  divisor_b = 0
  for divisor in divisores_b:
    divisor_b = divisor_b + divisor
  print(divisor_b)

  if divisor_b == a and divisor_a == b:
    return True 
  else:
    return False
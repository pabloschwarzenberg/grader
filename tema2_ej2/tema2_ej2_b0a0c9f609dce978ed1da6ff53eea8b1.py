# completa el código de la función
def amigos(a,b):
  divisor = 1
  suma_divisores_a = 0
  suma_divisores_b = 0
  while divisor < a or divisor < b :
    if divisor < a:
      if a % divisor == 0:
        suma_divisores_a += divisor
    if divisor < b:
      if b % divisor == 0:
        suma_divisores_b += divisor
    divisor += 1
  print("A::" + str(suma_divisores_a))
  print("B::" + str(suma_divisores_b))
  if suma_divisores_a == b or suma_divisores_b == a and suma_divisores_a > 1 and suma_divisores_b > 1:
    return True
  else:
    return False
           
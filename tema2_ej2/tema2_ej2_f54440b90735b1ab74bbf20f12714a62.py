def amigos(a, b):
  divisores_a = []
  divisores_b = []
  for n in range(1, a):
    if a % n == 0:
      divisores_a.append(n)
  for n in range(1, b):
    if b % n == 0:
      divisores_b.append(n)
  
  suma_a= 0
  suma_b = 0
  for n in divisores_a:
    suma_a += n
  for n in divisores_b:
    suma_b += n

  if suma_a == b and suma_b == a:
    return True
  else:
    return False
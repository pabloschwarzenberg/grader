def numero_perfecto(a):
  divisores = []
  suma = 0
  for i in range(1, a):
    if a % i == 0 and a != i:
      divisores.append(i)
      suma += i
  if suma == a:
    return True
  else:
    return False

  return divisores
           
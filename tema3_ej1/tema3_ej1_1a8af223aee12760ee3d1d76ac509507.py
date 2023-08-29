def suma_divisores(a):
  suma = 0
  for i in range(1, a - 1):
    division = a % i
    if division != 0:
      continue
    suma += i
  if suma == 1:
    primo = True
  else:
    primo = False
  
  return suma, primo

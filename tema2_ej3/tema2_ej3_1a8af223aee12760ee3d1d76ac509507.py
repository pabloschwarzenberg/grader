def numero_perfecto(a):
  suma = 0
  for i in range(1, a - 1):
    division = a % i
    if division == 0:
      suma = suma + 1
  if suma == a:
    num_perfecto = True
  else:
    num_perfecto = False
  return num_perfecto
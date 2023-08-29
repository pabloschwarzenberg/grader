def numero_perfecto(a):
  suma = 0
  for i in range(1, a-1):
    resto = a % i
    if resto == 0:
      suma += i
    if suma == a:
      perfecto = True
    else:
      perfecto = False
  return perfecto

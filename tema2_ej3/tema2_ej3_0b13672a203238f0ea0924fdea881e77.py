def numero_perfecto(a):
  SUMA = 0
  for i in range(1, a-1):
    RESTO = a % i
    if RESTO == 0:
      SUMA += i
  if SUMA == a:
    numperfect = 1
  else:
    numperfect = 0
  return numperfect







           
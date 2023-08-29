def numero_perfecto(numero):
  su = 0
  for i in range(1,numero):
    if (numero % (i) == 0):
      su += (i)
  if numero == su:
    return True
  else:
    return False
def numero_perfecto(a):
  diviso = []
  noprimo = False
  for divis in range(1, a):
    if a % divis == 0:
      diviso.append(divis)
  suma = sum(diviso)
  if sum(diviso) == a:
    return True
  else:
    return False
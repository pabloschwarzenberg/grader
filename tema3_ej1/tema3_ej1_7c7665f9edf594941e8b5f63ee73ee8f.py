def suma_divisores(a):
  diviso = []
  noprimo = False
  for divis in range(1, a):
    if a % divis == 0:
      diviso.append(divis)
  suma = sum(diviso)
  for num in range (2, suma):
    if suma % num == 0:
      noprimo = True
  if suma == 1:
      noprimo = True
  return suma, noprimo
  
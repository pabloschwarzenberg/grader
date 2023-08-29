def numero_perfecto(a):
  global lista1
  global suma
  global esperfecto
  suma = 0
  lista1 = []

  for i in range(1,a):
    if a%i==0:
      lista1.append(i)

  for i in lista1:
      suma = suma+i

  if suma ==a:
    esperfecto = True
  else:
    esperfecto=False

  return(esperfecto)



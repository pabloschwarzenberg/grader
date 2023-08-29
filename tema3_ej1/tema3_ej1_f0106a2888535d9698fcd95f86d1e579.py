# completa el código de la función
def suma_divisores(a):
  suma = 0
  for index in range(1, a-1):
    resto = a % index
    if resto != 0:
      continue
    suma += index
  if suma == 1:
    primo = True
  else:
    primo = False
  return suma, primo
           
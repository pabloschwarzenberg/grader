# completa el código de la función
def suma_divisores(a):
  suma = 0
  for i in range(1, a-1):
    resto = a % i
    if resto != 0:
      continue
    suma += i
  if suma == 1:
    primo = 1
  else:
    primo = 0
  return suma,primo
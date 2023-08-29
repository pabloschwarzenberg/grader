# completa el código de la función

def suma_divisores(n):
  suma = 0
  for i in range(1, n-1):
    resto = n%i
    if resto != 0:
      continue
    suma += i
  if suma == 1:
    primo = 1
  else:
    primo = 0
  return suma,  primo 

           
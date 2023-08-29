# por favor escribe aquí tu función
#Formula para ver los divisores de un numero 
def es_primo(x):
  i = 1
  contador = 0
  while i <= x:
    if x%i == 0:
      contador += 1
    i += 1
  if contador == 2:
    return True
  else:
    return False
           
# completa el código de la función
def suma_divisores(a):
  import math
  divisor = 1
  lista_divisores = []
  while divisor < a:
     if a%divisor == 0:
        lista_divisores.append(divisor)
     divisor += 1
  suma = math.fsum(lista_divisores)
  if suma == 1:
     estado = True
  else:
     estado = False
  return suma, estado
           
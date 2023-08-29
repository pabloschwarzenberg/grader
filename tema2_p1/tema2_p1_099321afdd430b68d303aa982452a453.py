# por favor escribe aquí tu función
#numero = int(input("ingrese un numero: "))

def es_primo(numero):
  z = 0
  for x in range(1,numero+1):
    if numero%x == 0:
      z = z+1
  if z == 2:
    return True
  else:
    return False

#es_primo(numero)
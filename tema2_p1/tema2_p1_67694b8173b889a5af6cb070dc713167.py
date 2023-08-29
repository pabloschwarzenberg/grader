# por favor escribe aquí tu función
def es_primo(numero):
  cont = 0
  for x in range(1, numero + 1):
     if numero % x == 0:
       cont += 1
       
  if cont == 2:
    return True
  else:
    return False
  return
           
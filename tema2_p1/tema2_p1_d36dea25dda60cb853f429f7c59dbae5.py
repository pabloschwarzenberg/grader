# por favor escribe aquí tu función
def es_primo(numero):
  divisor = 1
  cont = 0
  while divisor <= numero:
    resto = numero%divisor
    divisor += 1
    if resto == 0:
      cont += 1
  if cont == 2:
    return(True)
  else: 
    return(False)

           
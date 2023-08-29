def esPrimo(numero):

  if (numero == 1):
    return True
  if (numero < 1):
    return False

  if (primerPrimoDeUnNumero(numero) == numero) :
    return True
  return False

def primerPrimoDeUnNumero(n):
  primo = 2
  while ((n%primo) != 0):
    primo += 1
  return primo


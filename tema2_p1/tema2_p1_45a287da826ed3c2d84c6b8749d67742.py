# por favor escribe aquí tu función
def es_primo(numero):

  if numero < 2:

    return False

  for n in range(2, numero):

    if numero % n == 0:

      return False

    else:

      return True

           
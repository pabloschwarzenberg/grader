# por favor escribe aquí tu función
def es_primo(numero):
  return True if numero > 1 and all(numero % i != 0 for i in range(2, numero)) else False
           
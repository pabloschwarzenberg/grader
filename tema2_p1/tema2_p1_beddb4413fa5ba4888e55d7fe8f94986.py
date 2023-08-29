# por favor escribe aquí tu función
def es_primo(numero):
  i = 2
  while i < numero**0.5:
    if not numero%i:
      return False
    i+=1
  return True if numero != 1 else False
           
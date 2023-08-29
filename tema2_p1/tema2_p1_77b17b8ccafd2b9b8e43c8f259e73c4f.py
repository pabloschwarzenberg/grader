# por favor escribe aquí tu función
def es_primo(numero):
  es_primo = True
  if(numero != 1):
    for i in range(2, numero):
      if(numero%i == 0):
        es_primo = False
  else:
    es_primo = False
  return es_primo
           
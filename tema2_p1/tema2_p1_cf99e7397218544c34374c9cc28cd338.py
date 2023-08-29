# por favor escribe aquí tu función
def es_primo(numero):
  if numero > 1:
    for i in range(2,numero):
      if(numero % i) == 0:
        es_primo = False
        break
      else:
        es_primo = True
  else:
    es_primo = False
  return es_primo
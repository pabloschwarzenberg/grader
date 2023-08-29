def es_primo(numero):
  if numero > 1:
    for x in range(2,numero):
      if(numero % x) == 0:
        es_primo = False
        break
      else:
        es_primo = True
  else:
    es_primo = False
  return es_primo

# por favor escribe aquí tu función
def es_primo(numero):
  lst = list()
  for i in range(1, numero+1):
    if numero % i == 0:
      lst.append(i)
  if len(lst) == 2:
    return True
  else:
    return False
           
# por favor escribe aquí tu función
def es_primo(numero):
  r = True
  if numero==(0 or 1):
    r = False
  else:
    for i in range(2,numero//2+1):
      if numero%i==0:
        r = False
        i+1
      else:
        r = True
  return r    
# por favor escribe aquí tu función
def es_primo(numero):
  if numero <= 1:
    return False
  else:
    for i in range(2,numero-1):
        if numero%i==0:
            return False

  if numero%1==0 and numero%numero==0:
    return True
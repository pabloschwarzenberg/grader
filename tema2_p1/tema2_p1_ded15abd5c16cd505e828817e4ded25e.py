# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
      return False
    else:
      for m in range(2,numero):
         if numero%m==0:
             return False
         else:
             return True

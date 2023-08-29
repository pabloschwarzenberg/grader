# por favor escribe aquí tu función
def es_primo(numero):
    if numero ==1:
        return False
    elif numero== 2:
        return True
    else:
         for j in range(2, numero):
             if numero % j == 0:
                  return False
         return True
           
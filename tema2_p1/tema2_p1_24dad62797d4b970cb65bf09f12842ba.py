# por favor escribe aquí tu función
def es_primo(Numero):
  
    if Numero <= 1:
        return False
    elif Numero == 2:
        return False
    else:
        for i in range(2,Numero):
            if Numero % i == 0:
                return False
        return True
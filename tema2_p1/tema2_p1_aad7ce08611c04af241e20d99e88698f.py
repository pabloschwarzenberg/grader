# por favor escribe aquí tu función

def es_primo(numero):
    
    n = 2
    if numero == 1:
      return False
   
    while n < numero:
        if numero % n == 0:
            return False
        n+=1
    return True

           
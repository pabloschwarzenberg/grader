def es_primo(numero):
    if numero<2:
        return False
    else:
      for a in range(2,numero):
         if numero%a==0:
            return False
         else:
            return True
            

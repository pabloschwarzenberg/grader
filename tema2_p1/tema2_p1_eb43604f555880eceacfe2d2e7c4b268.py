# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
      return False
    else:
     n=2
     while (numero%n)!=0:
      if n==(numero-1):
         return True
         break
      else:
        n+=1
     return False
           
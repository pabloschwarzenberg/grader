# por favor escribe aquí tu función
def es_primo(numero1):
 #calculo
 if numero1 < 2:
   return False
 for i in range(2, numero1):
   if numero1% i == 0: 
  #return  
    return False
 
 return True

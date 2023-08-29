#ENTRADA
def es_primo(numero):
#DESARROLLO
 if numero < 2: 
   return False
 for i in range(2, numero):
   if numero % i == 0: 
#SALIDA   
    return False
 return True 

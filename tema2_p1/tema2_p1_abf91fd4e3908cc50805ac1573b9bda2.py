# por favor escribe aquí tu función
def es_primo(numero):
  
 if not numero == 1:
  for N in range(2,numero-1):
    if numero%N==0:
      return False
  
    return True
 if not numero == 3:
   for N in range(2,numero-1):
    if numero%N==0:
      return False
  
    return True
 if numero == 3:
   return True
 if numero == 1:
   return False
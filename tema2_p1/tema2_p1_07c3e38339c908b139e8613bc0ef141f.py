# por favor escribe aquí tu función
def divisores(numero):
   divisor=1
   cantidaddivisores=0
   while divisor<=numero:
        if numero%divisor==0:
            cantidaddivisores=cantidaddivisores+1
        divisor=divisor+1
   return cantidaddivisores
   
def es_primo(numero): 
  if (divisores(numero)==2):
    return True
  else:
    return False


           
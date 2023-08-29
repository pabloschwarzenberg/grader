# por favor escribe aquí tu función
import math
numero=int(input("Numero:"))
def es_primo(numero):
   if numero==1: 
      return("False")
   i=2
   while 1<i<numero:
      if numero%i==0:
         return("False")
      i=i+1
   return("True")
print(es_primo(numero))


           
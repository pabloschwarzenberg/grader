#Conversión de Decimal a Binario
import math

n = int(input("Ingrese el numero : "))
binario = " "
if (n>0):
  
  while(n>0):
    
     if (n%2 == 0):
         binario = "0" + binario
     else:
         binario = "1" + binario
     n = int(math.floor(n/2)) 
print("resultado =",binario)
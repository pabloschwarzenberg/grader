#Conversión de Decimal a Binario
numero_decimal=int(input("ingrese numero decimal:"))
bits = 1
Binario = ""

while True:
  if(2**bits)-1 >=numero_decimal:
     break
  bits = bits + 1
  
n = bits - 1
suma = 0
while n >= 0:
  if suma + (2**n) <= numero_decimal:
     Binario = Binario + "1"
     suma= suma + 2 ** n
  else:
     Binario = Binario + "0"
  n = n - 1
print ("resultado=",Binario)  
  
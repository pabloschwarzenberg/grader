decimal = int(input("Ingresa un número decimal: "))
binario =""
while decimal > 0:
 residuo = int(decimal % 2)
 decimal = int(decimal / 2)
 binario = str(residuo) + binario
   
print( "Resultado=",(binario) )
  
#Conversión de Decimal a Binario
decimal= float(input("ingresa un numero decimal: "))
if decimal <= 0:
  print("0")
binario= ""
while decimal > 0:
  residuo= int(decimal % 2)
  decimal= int(decimal / 2)
  binario= str(residuo) + binario
print(binario)
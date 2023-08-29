#Conversión de Decimal a Binario
ingreso = int(input("Número a convertir: "))
binario=bin(ingreso).replace("0b", "")
print ("resultado=", binario)
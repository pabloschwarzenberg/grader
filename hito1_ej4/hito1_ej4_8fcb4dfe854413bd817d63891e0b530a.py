#Conversión de Decimal a Binario
decimal = int(input("Ingrese un numero decimal para transformarlo a numero binario: "))
bin(decimal)
binario = int(bin(decimal)[2:])
print("resultado=",binario)
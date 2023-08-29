#Conversión de Decimal a Binario
numero=int(input("ingrese un numero:"))
binario=bin(numero)
bin=str(binario)


print("resultado=",bin.replace('0b','') )      
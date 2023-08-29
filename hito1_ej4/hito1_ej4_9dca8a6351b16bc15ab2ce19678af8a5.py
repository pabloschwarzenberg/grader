#Conversión de Decimal a Binario
num = int(input("Ingrese un numero: "))
binario = bin(num)
binario = str(binario)
print("resultado="+binario[2:])
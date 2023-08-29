#Conversión de Decimal a Binario
num=int(input("Ingrese numero: "))
numBin= bin(num)
print("resultado=",(numBin.replace("0b", "")))
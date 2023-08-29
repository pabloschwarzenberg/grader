#Conversión de Decimal a Binario
num = float(input("Ingresa un numero: "))

binario = bin(int(num))[2:]

print("resultado="+binario)
#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))

binario = ""
while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2

print("resultado =", binario)
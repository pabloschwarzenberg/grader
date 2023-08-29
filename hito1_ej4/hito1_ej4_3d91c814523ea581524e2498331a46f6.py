#Conversión de Decimal a Binario
decimal=int(input("ingrese numero"))
binario = ''
while decimal // 2 != 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
print("resultado="+str(decimal) + binario)
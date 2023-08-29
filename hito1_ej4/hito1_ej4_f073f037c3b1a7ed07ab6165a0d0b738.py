#Conversión de Decimal a Binario
decimal = int(input("Ingrese numero decinal: "))
resultado = ''
while decimal // 2 != 0:
    resultado = str(decimal % 2) + resultado
    decimal = decimal // 2
resultado = str(decimal) + resultado
print("resultado=",resultado)
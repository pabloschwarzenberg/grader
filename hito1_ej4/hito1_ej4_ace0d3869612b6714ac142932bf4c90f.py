#Conversión de Decimal a Binario
decimal = int(input("Ingrese Numero Decimal : "))
binario = ''
while decimal // 2 != 0:
   binario = str(decimal % 2) + binario
   decimal = decimal // 2
resultado = str(decimal)+ binario
print("resultado = ", resultado)
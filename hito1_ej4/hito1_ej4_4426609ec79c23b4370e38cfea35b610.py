#Conversión de Decimal a Binario
decimal = float(input("Ingresa un número: "))
binario = ""
while decimal > 0:
        res = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(res) + binario
print("resultado="+ binario)
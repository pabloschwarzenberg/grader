#Conversión de Decimal a Binario
decimal = int(input("Ingresa un número decimal: "))
binario = ""
if decimal == 0:
    binario = "0"
else:
    while decimal > 0:
        digito = decimal % 2
        binario = str(digito) + binario       
        decimal = decimal // 2

print("resultado =", binario)

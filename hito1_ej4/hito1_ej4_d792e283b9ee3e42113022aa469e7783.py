decimal = int(input("Ingresa un número decimal: "))
binario = ""
if decimal < 0:
    binario = 0
while decimal > 0:
    residuo = int (decimal % 2)
    decimal = int (decimal / 2)
    binario = str(residuo)+ binario
print('resultado =', binario)
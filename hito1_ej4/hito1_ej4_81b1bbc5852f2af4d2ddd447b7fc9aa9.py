#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))
binario = ""
cociente = numero_decimal
while cociente > 0:
    residuo = cociente % 2
    cociente = cociente // 2
    binario = str(residuo) + binario

print("Resultado =", binario)      
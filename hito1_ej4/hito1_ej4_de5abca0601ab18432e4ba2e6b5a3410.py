#Conversión de Decimal a Binario
numero = int(input("introduce el numero decimal: "))
binario = ""
while numero // 2 != 0:
    binario = str(numero % 2) + binario
    numero = numero//2
print("resultado =", str(numero) + binario)
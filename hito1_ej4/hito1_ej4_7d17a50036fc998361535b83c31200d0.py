#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))
es_negativo = False
if decimal < 0:
    es_negativo = True
    decimal = abs(decimal)

binario = ""
while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2

if es_negativo:
    binario = "-" + binario

print("resultado =", binario)      
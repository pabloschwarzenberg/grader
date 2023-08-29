#Conversión de Decimal a Binario
numeroDecimal = int(input('Introduce el número a convertir a binario: '))
binario = ""
while numeroDecimal > 0:
    numero = numeroDecimal % 2
    numeroDecimal = numeroDecimal // 2
    binario = str(numero) + binario
print("resultado =",binario)
#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es negativo
es_negativo = False
if decimal < 0:
    es_negativo = True
    decimal = abs(decimal)

# Realizar la conversión a binario
binario = ""
while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2

# Agregar el signo negativo si es necesario
if es_negativo:
    binario = "-" + binario

print("resultado =", binario)
      
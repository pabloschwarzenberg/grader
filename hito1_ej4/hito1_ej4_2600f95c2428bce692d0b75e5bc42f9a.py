#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es negativo
es_negativo = False
if numero_decimal < 0:
    es_negativo = True
    numero_decimal = abs(numero_decimal)

# Convertir a binario
binario = bin(numero_decimal)[2:]

# Agregar el signo negativo si es necesario
if es_negativo:
    binario = "-" + binario

# Imprimir el resultado
print("resultado =", binario)
     
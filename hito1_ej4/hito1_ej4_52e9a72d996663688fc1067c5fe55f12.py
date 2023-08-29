#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es negativo
es_negativo = False
if numero_decimal < 0:
    es_negativo = True
    numero_decimal = abs(numero_decimal)

# Realizar la conversión a binario
resultado_binario = bin(numero_decimal)[2:]

# Agregar el signo "-" si el número era negativo
if es_negativo:
    resultado_binario = "-" + resultado_binario

print("Resultado =", resultado_binario)
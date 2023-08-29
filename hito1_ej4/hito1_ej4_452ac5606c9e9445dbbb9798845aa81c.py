# Conversión de Decimal a Binario
# Obtener el número decimal del usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Realizar la conversión a binario
binario = ""
while numero_decimal > 0:
    residuo = numero_decimal % 2
    binario = str(residuo) + binario
    numero_decimal = numero_decimal // 2

# Imprimir el resultado
print("Resultado =", binario)

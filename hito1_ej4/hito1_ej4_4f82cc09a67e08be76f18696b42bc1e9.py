#Conversión de Decimal a Binario
# Solicitar al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Inicializar una variable para almacenar el resultado binario
resultado_binario = ''

# Verificar si el número es 0, en ese caso el resultado es '0'
if numero_decimal == 0:
    resultado_binario = '0'
else:
    # Convertir el número decimal a binario
    while numero_decimal > 0:
        digito_binario = numero_decimal % 2
        resultado_binario = str(digito_binario) + resultado_binario
        numero_decimal = numero_decimal // 2

# Imprimir el resultado
print("Resultado =", resultado_binario)
      
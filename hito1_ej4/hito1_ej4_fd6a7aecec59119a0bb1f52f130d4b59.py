#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    resultado = ""
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero = numero // 2
    return resultado

# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado_binario)
      
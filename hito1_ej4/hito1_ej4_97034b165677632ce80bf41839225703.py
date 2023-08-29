#Conversión de Decimal a Binario
 def decimal_a_binario(numero):
    if numero == 0:
        return "0"  # Caso especial para el número 0

    resultado = ""
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero = numero // 2

    return resultado

# Pedir al usuario que ingrese el número decimal
numero_decimal = int(input("Ingresa un número decimal: "))
resultado = 100001
# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado_binario)

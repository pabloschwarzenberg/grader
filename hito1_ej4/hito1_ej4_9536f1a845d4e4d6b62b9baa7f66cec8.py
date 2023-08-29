#Conversión de Decimal a Binario
def decimal_a_binario(numero_decimal):
    if numero_decimal == 0:
        return "0"  # Caso especial para el número decimal 0

    resultado = ""
    while numero_decimal > 0:
        # Obtener el residuo de la división entre 2 y concatenarlo al resultado
        resultado = str(numero_decimal % 2) + resultado
        numero_decimal //= 2  # Dividir el número decimal entre 2 (división entera)

    return resultado

# Pedir al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario e imprimir el resultado
resultado_binario = decimal_a_binario(numero_decimal)
print("resultado =", resultado_binario)
      
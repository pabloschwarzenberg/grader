#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    # Verificar si el número es cero
    if decimal == 0:
        return '0'

    # Crear una lista para almacenar los dígitos binarios
    binario = []

    # Convertir el número decimal a binario
    while decimal > 0:
        residuo = decimal % 2
        binario.append(str(residuo))
        decimal //= 2

    # Invertir la lista binaria y convertirla a cadena
    binario.reverse()
    resultado = ''.join(binario)

    return resultado


# Obtener el número decimal ingresado por el usuario
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado_binario)
      
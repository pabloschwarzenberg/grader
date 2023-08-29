#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    # Verificar si el número es cero
    if numero == 0:
        return '0'

    # Lista para almacenar los dígitos binarios
    digitos = []

    # Obtener el valor absoluto del número
    numero = abs(numero)

    # Convertir el número a binario
    while numero > 0:
        residuo = numero % 2
        digitos.append(str(residuo))
        numero = numero // 2

    # Invertir la lista de dígitos binarios
    digitos.reverse()

    # Unir los dígitos en un solo número binario
    resultado = ''.join(digitos)

    return resultado


# Obtener el número decimal de entrada
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado_binario)

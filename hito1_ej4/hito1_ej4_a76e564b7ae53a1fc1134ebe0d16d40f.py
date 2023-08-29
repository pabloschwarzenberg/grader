#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    # Verificar si el número es 0
    if numero == 0:
        return "0"

    binario = ""
    while numero > 0:
        # Obtener el residuo de la división entre 2
        residuo = numero % 2
        # Agregar el residuo al inicio del número binario
        binario = str(residuo) + binario
        # Dividir el número entre 2 para continuar con la siguiente iteración
        numero = numero // 2

    return binario

# Obtener el número decimal desde el usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", numero_binario)

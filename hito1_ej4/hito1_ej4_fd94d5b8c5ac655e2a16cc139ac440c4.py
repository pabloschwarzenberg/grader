def decimal_a_binario(numero):
    """
    Función para convertir un número decimal a binario.

    Argumento:
    - numero: número decimal a convertir

    Retorna:
    - resultado: representación binaria del número decimal
    """
    resultado = bin(numero)[2:]  # Utilizamos la función bin() para obtener la representación binaria
    return resultado

# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Mostrar el resultado
print("Resultado =", resultado_binario)

      
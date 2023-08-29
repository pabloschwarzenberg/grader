def decimal_a_binario(numero):
    # Verificar si el número es cero
    if numero == 0:
        return '0'

    # Realizar la conversión a binario
    binario = ''
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    return binario


if __name__ == "__main__":
    # Solicitar al usuario ingresar el número decimal
    decimal = int(input("Ingrese un número decimal: "))

    # Llamar a la función para convertir a binario
    binario = decimal_a_binario(decimal)

    # Imprimir el resultado
    print("resultado =", binario)
      
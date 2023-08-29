def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Utilizamos la función bin() para obtener la representación binaria y omitimos los primeros dos caracteres "0b"
    return binario


# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado)

      
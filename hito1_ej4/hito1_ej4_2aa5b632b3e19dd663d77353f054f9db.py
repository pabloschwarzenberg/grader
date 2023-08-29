def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Utilizamos la función bin() y omitimos los dos primeros caracteres "0b"
    return binario

# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado=" + resultado)

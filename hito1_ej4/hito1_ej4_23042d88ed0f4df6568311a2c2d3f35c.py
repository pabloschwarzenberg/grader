def decimal_a_binario(numero):
    resultado = bin(numero)[2:]  # Utilizamos la función bin() para obtener la representación binaria y eliminamos los dos primeros caracteres "0b"
    return resultado

# Solicitar entrada al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Llamar a la función y mostrar el resultado
resultado_binario = decimal_a_binario(numero_decimal)
print("resultado=" + resultado_binario)


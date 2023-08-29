numero_decimal = int(input("Ingrese un número decimal: "))
resultado = ''

# Verificar si el número es cero
if numero_decimal == 0:
    resultado = '0'
else:
    # Realizar la conversión a binario mediante divisiones sucesivas
    while numero_decimal > 0:
        # Obtener el residuo de la división por 2
        residuo = numero_decimal % 2
        # Concatenar el residuo al resultado
        resultado = str(residuo) + resultado
        # Actualizar el número dividiéndolo entre 2
        numero_decimal = numero_decimal // 2

print("Resultado:", resultado)

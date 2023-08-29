# Pedir al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario utilizando el formato binario de Python y eliminar el prefijo "0b"
numero_binario = format(numero_decimal, "b")

# Imprimir el resultado
print("El número binario correspondiente es: resultado =", numero_binario)

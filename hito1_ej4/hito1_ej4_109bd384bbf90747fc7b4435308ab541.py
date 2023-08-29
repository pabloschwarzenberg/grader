## Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario utilizando la función bin()
numero_binario = bin(numero_decimal)

# Obtener la representación binaria eliminando el prefijo "0b"
representacion_binaria = numero_binario[2:]

# Imprimir el resultado
print("resultado =", representacion_binaria)
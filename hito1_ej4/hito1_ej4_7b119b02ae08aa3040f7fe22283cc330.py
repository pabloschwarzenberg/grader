#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

# Utilizamos la función bin() para convertir el número decimal a binario
numero_binario = bin(numero_decimal)

# El resultado de la función bin() incluye el prefijo "0b", lo eliminamos con un slicing [2:]
numero_binario = numero_binario[2:]

print("resultado =", numero_binario)
     
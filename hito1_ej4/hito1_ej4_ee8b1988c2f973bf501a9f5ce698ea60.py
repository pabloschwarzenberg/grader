# Solicitar el número decimal al usuario
decimal = int(input("Ingrese un número decimal: "))

# Realizar la conversión a binario
binario = bin(decimal)[2:]  # La función bin() devuelve el número binario con el prefijo '0b', por lo que se eliminan los primeros dos caracteres [2:]

# Imprimir el resultado
print("resultado =", binario)

      
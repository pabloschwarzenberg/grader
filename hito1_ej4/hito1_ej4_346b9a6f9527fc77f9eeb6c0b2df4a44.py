decimal = int(input("Ingrese un número decimal: "))

# Utilizamos la función bin() para obtener la representación binaria del número decimal
binario = bin(decimal)

# Obtenemos el resultado eliminando el prefijo '0b' que indica que es un número binario en Python
resultado = binario[2:]

print("Resultado =", resultado)
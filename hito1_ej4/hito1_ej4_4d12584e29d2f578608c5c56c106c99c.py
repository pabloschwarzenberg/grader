# Obtener el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
binario = bin(decimal)[2:]  # Utilizamos la función bin() y eliminamos los primeros dos caracteres "0b"

# Imprimir el resultado
print("resultado =", binario)
      
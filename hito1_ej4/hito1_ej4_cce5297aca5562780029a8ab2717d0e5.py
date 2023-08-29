# Solicitar número decimal al usuario
decimal = int(input("Ingrese un número decimal: "))

# Convertir decimal a binario
binario = bin(decimal)[2:]  # Utilizamos la función bin() para convertir a binario y omitimos los primeros dos caracteres ('0b')

# Imprimir resultado
print("Resultado:", binario)
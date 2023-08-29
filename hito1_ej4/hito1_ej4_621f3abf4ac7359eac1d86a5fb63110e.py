#Conversión de Decimal a Binario
# Solicitar al usuario el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario = bin(decimal)[2:]  # La función bin() convierte a binario y agrega el prefijo '0b', se remueve con [2:]

# Imprimir el resultado
print("resultado =", binario)
#Conversión de Decimal a Binario
# Solicitar al usuario ingresar el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario usando la función bin()
binario = bin(decimal)

# Extraer el valor binario de la cadena generada por la función bin()
# Se omite los dos primeros caracteres "0b" que indican que es binario
binario = binario[2:]

# Imprimir el resultado
print("resultado =", binario)

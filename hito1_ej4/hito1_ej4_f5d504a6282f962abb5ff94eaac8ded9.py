#Conversión de Decimal a Binario
# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario utilizando la función bin()
numero_binario = bin(numero_decimal)

# Extraer el resultado en formato de cadena de caracteres
resultado = numero_binario[2:]

# Imprimir el resultado
print("resultado =", resultado)
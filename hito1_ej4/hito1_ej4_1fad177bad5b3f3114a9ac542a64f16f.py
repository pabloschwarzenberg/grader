#Conversión de Decimal a Binario

numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario

numero_binario = bin(numero_decimal)

# Extraer el resultado binario sin el prefijo "0b"

resultado = numero_binario[2:]

# Imprimir el resultado

print("resultado =", resultado)

      
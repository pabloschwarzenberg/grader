#Conversión de Decimal a Binario
  # Obtener el número decimal del usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = bin(numero_decimal)[2:]  # Eliminar el prefijo "0b" del resultado

# Imprimir el número binario resultante
print("resultado =", numero_binario)    
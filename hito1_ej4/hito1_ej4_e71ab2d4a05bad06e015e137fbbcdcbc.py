#Conversión de Decimal a Binario
      # Obtener el número decimal del usuario
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario = bin(decimal)[2:]

# Imprimir el resultado
print("Resultado =", binario)

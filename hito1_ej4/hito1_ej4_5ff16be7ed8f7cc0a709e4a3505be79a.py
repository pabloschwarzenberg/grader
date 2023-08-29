#Conversión de Decimal a Binario
      # Solicitar al usuario ingresar un número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario = bin(decimal)[2:]

# Imprimir el resultado
print("resultado =", binario)
#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))

binario = bin(decimal)[2:]  # Convertir a binario y eliminar el prefijo "0b"

print("Resultado =", binario)
      
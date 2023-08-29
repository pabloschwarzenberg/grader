#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))

binario = bin(decimal)[2:]  # Utilizamos la función bin() para convertir a binario y omitimos los dos primeros caracteres "0b"

print("Resultado =", binario)
      
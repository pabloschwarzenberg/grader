#Conversión de Decimal a Binario
 # Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = bin(numero_decimal)[2:]

# Mostrar el resultado
print("Resultado =", numero_binario)
     
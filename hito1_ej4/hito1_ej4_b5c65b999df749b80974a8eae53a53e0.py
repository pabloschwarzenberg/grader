#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es cero
if decimal == 0:
    resultado = "0"
else:
    resultado = ""

# Convertir el número decimal a binario
while decimal > 0:
    resultado = str(decimal % 2) + resultado
    decimal //= 2

print("Resultado =", resultado)      
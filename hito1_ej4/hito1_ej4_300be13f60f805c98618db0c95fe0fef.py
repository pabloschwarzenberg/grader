#Conversión de Decimal a Binario
decimal = int(input("Ingrese un número decimal: "))

# Inicializamos una lista vacía para almacenar los dígitos binarios
binario = []

# Verificamos si el número ingresado es cero
if decimal == 0:
    binario.append(0)

# Convertimos el número decimal a binario
while decimal > 0:
    binario.append(decimal % 2)
    decimal //= 2

# Invertimos la lista para obtener el resultado correcto
binario.reverse()

# Imprimimos el resultado
print("Resultado =", ''.join(map(str, binario)))
      
decimal = int(input("Ingresa un número decimal: "))

# Función para convertir decimal a binario
def decimal_a_binario(decimal):
    if decimal == 0:
        return 0
    else:
        return (decimal % 2) + 10 * decimal_a_binario(decimal // 2)

# Llamada a la función y muestra del resultado
resultado = decimal_a_binario(decimal)
print("resultado =", resultado)

print(decimal)
      
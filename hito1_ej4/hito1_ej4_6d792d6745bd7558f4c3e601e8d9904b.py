#Conversión de Decimal a Binario
# Pedir al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Inicializar una lista para almacenar los dígitos binarios
digitos_binarios = []

# Realizar la conversión a binario
while numero_decimal > 0:
    residuo = numero_decimal % 2
    digitos_binarios.append(str(residuo))
    numero_decimal = numero_decimal // 2


digitos_binarios.reverse()


resultado = ''.join(digitos_binarios)


print("Resultado =", resultado)
      
numero_decimal = int(input("Ingrese un número decimal: "))

# Realizar la conversión a binario utilizando divisiones sucesivas
resultado = ""
while numero_decimal > 0:
    residuo = numero_decimal % 2
    resultado = str(residuo) + resultado
    numero_decimal = numero_decimal // 2

print("Resultado =", resultado)

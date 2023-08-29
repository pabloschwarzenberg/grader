# Solicitar al usuario que ingrese el número decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir el número decimal a binario
binario = ""
if numero_decimal == 0:
    binario = "0"
else:
    while numero_decimal > 0:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2

# Imprimir el resultado
print("El número binario equivalente es:", binario)
# Pedir al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = ""

if numero_decimal == 0:
    numero_binario = "0"
else:
    while numero_decimal > 0:
        bit = numero_decimal % 2
        numero_binario = str(bit) + numero_binario
        numero_decimal = numero_decimal // 2

# Imprimir el resultado
print("El número binario es:", numero_binario)

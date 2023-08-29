#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = ""

if numero_decimal == 0:
    numero_binario = "0"
else:
    while numero_decimal > 0:
        bit = numero_decimal % 2
        numero_binario = str(bit) + numero_binario
        numero_decimal = numero_decimal // 2

print("Resultado =", numero_binario)      
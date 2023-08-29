numero_decimal = int(input("Ingrese un número decimal: "))
binario = ""

if numero_decimal == 0:
    binario = "0"
else:
    while numero_decimal > 0:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2

print("resultado =", binario)
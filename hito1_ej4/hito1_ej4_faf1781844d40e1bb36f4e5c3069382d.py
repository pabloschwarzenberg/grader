numero_decimal = int(input("Ingrese un número decimal: "))
resultado_binario = ""

if numero_decimal == 0:
    resultado_binario = "0"
else:
    while numero_decimal > 0:
        resultado_binario = str(numero_decimal % 2) + resultado_binario
        numero_decimal = numero_decimal // 2

print("Resultado =", resultado_binario)

  
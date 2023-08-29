numero_decimal = int(input("Ingresa un número decimal: "))
if numero_decimal == 0:
    numero_binario = '0'
else:
    numero_binario = ''
while numero_decimal > 0:
    residuo = numero_decimal % 2
    numero_binario = str(residuo) + numero_binario
    numero_decimal = numero_decimal // 2
print("resultado=",numero_binario)
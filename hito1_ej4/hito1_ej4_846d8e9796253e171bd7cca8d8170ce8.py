numero_decimal = int(input("Ingrese un número decimal: "))

es_negativo = False
if numero_decimal < 0:
    es_negativo = True
    numero_decimal = abs(numero_decimal)

resultado_binario = ""
while numero_decimal > 0:
    resultado_binario = str(numero_decimal % 2) + resultado_binario
    numero_decimal = numero_decimal // 2

if es_negativo:
    resultado_binario = "-" + resultado_binario

print("Resultado =", resultado_binario)

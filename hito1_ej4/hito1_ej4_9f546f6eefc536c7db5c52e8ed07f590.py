#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un numero decimal: "))

numero_es_negativo = False
if numero_decimal < 0:
    numero_es_negativo = True
    numero_decimal = abs(numero_decimal)

resultado_binario = ""
while numero_decimal > 0:
    resultado_binario = str(numero_decimal % 2) + resultado_binario
    numero_decimal = numero_decimal // 2
if numero_es_negativo:
    resultado_numero_binario = "-" + resultado_binario

print("Resultado =", resultado_binario)      
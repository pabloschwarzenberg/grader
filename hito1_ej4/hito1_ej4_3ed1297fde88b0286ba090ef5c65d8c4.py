numero_decimal = int(input())

es_negativo = False
if numero_decimal < 0:
    es_negativo = True
    numero_decimal = abs(numero_decimal)

resultado_binario = bin(numero_decimal)[2:]

if es_negativo:
    resultado_binario = "-" + resultado_binario

print("resultado=" + resultado_binario)

      
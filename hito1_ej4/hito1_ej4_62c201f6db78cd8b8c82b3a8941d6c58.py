numero_decimal = int(input("Ingresa un número decimal: "))

# Verificar si el número ingresado es negativo
es_negativo = False
if numero_decimal < 0:
    es_negativo = True
    numero_decimal = abs(numero_decimal)

# Convertir el número decimal a binario
resultado_binario = ""
while numero_decimal > 0:
    resultado_binario = str(numero_decimal % 2) + resultado_binario
    numero_decimal = numero_decimal // 2

# Agregar signo negativo si corresponde
if es_negativo:
    resultado_binario = "-" + resultado_binario

print("Resultado =", resultado_binario)

      
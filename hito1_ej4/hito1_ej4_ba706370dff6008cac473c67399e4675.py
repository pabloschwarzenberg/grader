#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es negativo
es_negativo = False
if numero_decimal < 0:
    es_negativo = True
    numero_decimal = abs(numero_decimal)

# Convertir el número decimal a binario
resultado = ""
while numero_decimal > 0:
    resultado = str(numero_decimal % 2) + resultado
    numero_decimal //= 2

# Agregar el signo negativo si corresponde
if es_negativo:
    resultado = "-" + resultado

print("resultado =", resultado)

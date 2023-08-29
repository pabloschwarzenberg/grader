#Conversión de Decimal a Binario
# Pedir al usuario el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Variables para almacenar el número binario y el cociente
binario = ""
cociente = numero_decimal

# Calcular el número binario
while cociente > 0:
    residuo = cociente % 2
    cociente = cociente // 2
    binario = str(residuo) + binario

# Imprimir el resultado
print("Resultado =", binario)
       
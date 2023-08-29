#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

resultado = ""
cociente = numero_decimal

while cociente > 0:
    residuo = cociente % 2
    cociente = cociente // 2
    resultado = str(residuo) + resultado

print("resultado =", resultado)
     
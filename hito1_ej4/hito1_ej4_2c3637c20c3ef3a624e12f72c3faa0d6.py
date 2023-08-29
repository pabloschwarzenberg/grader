#Conversión de Decimal a Binario
numero_decimal = float(input("ingrese el numero: "))
numero_binario = 0
multiplicador = 1
while numero_decimal != 0:
    numero_binario = numero_binario + numero_decimal % 2 * multiplicador
    numero_decimal //= 2
    multiplicador *= 10
    numero_binario=round(numero_binario)
print("resultado="+ str(numero_binario))
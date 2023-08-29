# Conversión de Decimal a Binario
numero_decimal = int(input("ingrese un numero: "))

numero_binario = 0
multiplicador = 1
# Proceso del número
while numero_decimal != 0:
    numero_binario = numero_binario + numero_decimal % 2 * multiplicador
    numero_decimal //= 2
    multiplicador *= 10
# Resultado
print("resultado=", numero_binario)      
#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

if numero_decimal == 0:
    resultado = '0'
else:
    resultado = ''

    while numero_decimal > 0:
        resultado = str(numero_decimal % 2) + resultado
        numero_decimal //= 2
print("Resultado =", resultado)
      
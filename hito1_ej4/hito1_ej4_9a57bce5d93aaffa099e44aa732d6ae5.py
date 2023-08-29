#Conversión de Decimal a Binario
numero_decimal = int(input('ingresar un numero decimal: '))
#realizar la conversion 
numero_binario = ''
while numero_decimal > 0:
    residuo = numero_decimal % 2
    numero_binario = str(residuo) + numero_binario
    numero_decimal = numero_decimal // 2
print('resultado =', numero_binario)
      
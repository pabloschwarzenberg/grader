#Conversión de Decimal a Binario
numero = int(input('Introduce el número Decimal: '))
binario = ''
while numero >= 1:
  b = numero%2
  numero = numero//2
  binario = str(b)+binario
print('resultado= ',binario)
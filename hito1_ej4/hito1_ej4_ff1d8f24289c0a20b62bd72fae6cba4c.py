#Conversión de Decimal a Binario
decimal = int(input('que numero desea pasar a binario: '))
binario = ''
while decimal // 2 != 0:
  binario = str(decimal % 2) + binario
  decimal = decimal // 2
  x=str(decimal) + binario
print( 'resultado=', x)      
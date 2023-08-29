#Conversión de Decimal a Binario
decimal = eval(input('decimal: '))
binario = ''
while decimal>0:
  modulo = decimal%2
  binario = str(modulo)+binario
  decimal = decimal //2
print('resultado=',binario)

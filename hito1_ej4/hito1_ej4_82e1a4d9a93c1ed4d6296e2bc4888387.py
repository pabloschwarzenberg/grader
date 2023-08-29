#Conversión de Decimal a Binario
decimal = int(input('Ingrese un número: '))

cociente = decimal
binario_parcial = ''
while cociente > 0:
  resto = cociente % 2
  cociente = cociente // 2

  d_binario = str(resto)
  binario_parcial += d_binario

#Inversión de resultado
binario = ''
z = 1
for i in binario_parcial:
  binario += binario_parcial[len(binario_parcial)-z]
  z += 1

print()
print('resultado=', binario, sep='')


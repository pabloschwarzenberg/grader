#Conversión de Decimal a Binario
print('Ingrese un número')
n = int(input(':'))
division = n // 2
resto1 = n % 2
resultado = ''
while division >= 2:
  resto = division % 2
  division = division // 2
  resultado = str(resto) + resultado
  if division == 1:
    resultado = str(division) + resultado 
print('resultado =', resultado + str(resto1))

#Contestador de celular
numero = int(input('Ingrese un número telefónico: '))
hora = int(input('Ingrese una hora: '))

x = [numero]

if hora >= 20:
  print('No contestar')
elif hora >= 0 and hora <= 7:
  print('Contestar')
elif hora < 14:
  print('Contestar')
elif hora >= 17 and hora <= 19:
  print('No contestar')
elif x[5] == 9 and x[6] == 0 and x[7] == 9:
  print('Contestar')


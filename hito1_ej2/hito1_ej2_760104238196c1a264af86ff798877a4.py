#Contestador de celular
numero = input('Ingrese numero telefonico: ')
hora = int(input('Ingrese hora de la llamada: '))
if (hora <= 7) or (hora < 14 and numero[-3:] == '909') or (hora >= 17 and hora <= 19 and numero[:3] != '877'):
  print('Resultado: CONTESTAR')
else:
  print('Resultado: NO CONTESTAR')

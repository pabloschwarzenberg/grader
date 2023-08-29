secuencia = input('Ingrese secuencia: ')
sCorrecta = True
for baseN in 'bdefhijklmnñopqrsuvwxyz':
      if baseN in secuencia :
            sCorrecta = False


if sCorrecta:
      print('secuencia correcta')
else:
      print('secuencia incorrecta')


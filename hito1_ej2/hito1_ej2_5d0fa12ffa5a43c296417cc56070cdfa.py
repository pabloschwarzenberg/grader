a = 'CONTESTAR'
b = 'NO CONTESTAR'

telefono = int(input('Ingrese numero telefonico: '))

hora = int(input('Ingrese hora de la llamada: '))

if(hora<=7):
  print('Resultado: ', a)

if(hora<=14 and hora>7):
    tele1 = telefono//1000
    sobrante = telefono%1000
    if(sobrante==909):
      print('Resultado: ', a)
    else:
      print('Resultado: ', b)
if(hora<=16 and hora>14):
    print('Resultado: ', b)

if(hora<=19 and hora>16):
    tele1 = telefono // 100000
    if(tele1==877):
        print('Resultado: ', b)
    else:
        print('Resultado: ', a)

if(hora>19):
    print('Resultado: ', b)
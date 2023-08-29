#Contestador de celular
telefono = int(input('Ingrese su numero (8 digitos):'))
hora = eval(input('Ingrese la hora del dia (0-23):'))

comi = telefono//100000
ulti = telefono%1000

if hora<=7 and hora>= 0:
  print ('CONTESTAR')
elif hora>19:
  print('NO CONTESTAR')
elif hora<14 and ulti==909:
  print('CONTESTAR')
elif hora>=17 and hora<=19 and comi!=877:
  print('CONTESTAR')
else:
    print('NO CONTESTAR')     
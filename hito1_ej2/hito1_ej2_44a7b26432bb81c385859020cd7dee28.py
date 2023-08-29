num=int(input('>>> Ingrese numero telefonico: '))
time=int(input('>>> Ingrese hora de la llamada: '))
list = (list(str(num)))
if time >= 0 and time <= 7:
  print('CONTESTAR')
elif time <= 14:
  if list[5] == '9' and list[6] == '0' and list[7] == '9':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
elif time >= 17 and time <= 19:
  if list[0] == '8' and list[1] == '7' and list[2] == '7':
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
elif time >= 19:
  print('NO CONTESTAR')
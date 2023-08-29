#Contestador de celular
Numero_telefonico = str(input('ingrese numero telefonico'))
Hora = int(input('ingrese la hora'))
num3final = int(Numero_telefonico[5:8])
num3inicial = int(Numero_telefonico[0:3])
print(Numero_telefonico[5:8])
if (Hora > 0)  and (Hora < 7):
  print('CONTESTAR')
elif (Hora > 7) and (Hora < 14):
  if (num3final == 909):
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
elif (Hora > 17) and (Hora < 19):
  if (num3inicial == 877):
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
elif Hora > 19:
  print('NO CONTESTAR')
 
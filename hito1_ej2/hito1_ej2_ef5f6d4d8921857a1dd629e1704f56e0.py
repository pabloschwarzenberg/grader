#Contestador de celular
phone = int(input('Ingrese número de teléfono: '))
day_time = int(input('Ingrese hora del día: '))

answer = 'CONTESTAR'
hang_up = 'NO CONTESTAR'

if 0 <= day_time <= 7:
  print(answer)
elif 7 < day_time <= 14:
  if phone % 1000 == 909:
    print(answer)
  else:
    print(hang_up)
elif 17 <= day_time <= 19:
  if phone // 100000 == 877:
    print(hang_up)
  else:
    print(answer)
else:
  print(hang_up)

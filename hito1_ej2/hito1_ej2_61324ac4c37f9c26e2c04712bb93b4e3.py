#Contestador de celular
numero=int(input('ingrese numero telefonico: '))
hora=int(input('ingrese hora de la llamada: '))

if 0<=hora<=7:
  print('contestar')
elif 7<hora<=14 and numero%1000 == 909:
  print('contestar')
elif 7<hora<=14:
   print('no contestar')
elif 17<hora<=19 and numero//100000 == 877:
  print('no contestar')
elif 17<hora<=19:
  print('contestar')
else:
  print('no contestar')
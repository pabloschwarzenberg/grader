#Contestador de celular
telefono = int(input("ingrese numero telefonico"))
hora = int(input("ingrese la hora de la llamada (sin minutos)"))
if 0<hora<7:
 print("contestar")
elif hora <14:
 if telefono[5:8] == 909:
  print("contestar")
 else:
  print("no contestar")
elif 17 < hora < 19:
 if telefono[5:8] == 877:
  print("contestar")
 else:
  print("no contestar")
elif hora > 19:
else:
 print("no contestar")
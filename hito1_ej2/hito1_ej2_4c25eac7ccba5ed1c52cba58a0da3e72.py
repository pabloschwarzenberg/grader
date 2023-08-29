#Contestador de celular
telefono=eval(input("Ingrese numero telefonico: "))
hora=eval(input("Ingrese hora de la llamada: "))
telefonoI=telefono//100000
telefonoF=telefono%1000
 
if hora>=0 and hora<=7:
  print("Resultado: CONTESTAR")

elif hora>=8 and hora<=14:
  if telefonoF==909:
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")

elif hora>=15 and hora<=16:
  print("Resultado: NO CONTESTAR")

elif hora>=17 and hora<=19:
  if telefonoI==877:
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: CONTESTAR")

elif hora>=20 and hora<=23:
  print("Resultado: NO CONTESTAR")

elif hora<=-1:
  print("Hora no existente.")
elif hora>=24:
  print("Hora no existente.")
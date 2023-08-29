#Contestador de celular
Numero_telefonico = int(input("Ingrese numero telefonico: "))
Hora = int(input("Ingrese la hora de llamada: "))
Diez_millon = ((Numero_telefonico)//10000000)
Millon = ((Numero_telefonico)//1000000)%10
Cienmil = ((Numero_telefonico)//100000)%10
Centena = ((Numero_telefonico)//100)%10
Decena = ((Numero_telefonico)//10)%10
Unidad = ((Numero_telefonico)//1)%10
if (Numero_telefonico > 9999999 and Numero_telefonico < 100000000 and Hora >= 0 and Hora <= 23):
  print("Numero y hora valido")
  if (Hora >= 0 and Hora <= 7):
      print("CONTESTAR")
  if (Hora > 7 and Hora <= 14):
    if (Centena == 9 and Decena == 0 and Unidad == 9):
      print("CONTESTAR")
    else:
      print("NO CONTESTAR")
  if (Hora >= 17 and Hora <= 19):
    if (Diez_millon == 8 and Millon == 7 and Cienmil == 7):
      print("NO CONTESTAR")
    else:
        print("CONTESTAR")
  if (Hora > 19):
    print("NO CONTESTAR")
else:
  print("Numero o hora invalido ")
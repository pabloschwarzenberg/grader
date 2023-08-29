#Contestador de celular
numberphone = int(input("Ingrese numero telefonico: "))
hour = int(input("Ingrese hora de la llamada: "))
if len(str(numberphone)) != 8:
  print("Error, ingrese un numero valido")
elif len(str(hour)) > 2:
  print("Error, ingrese una hora correcta")
else:
  if hour >= 0 and hour < 8:
            print("Resultado: CONTESTAR")
  elif hour > 7 and hour < 15:
    if numberphone % 1000 == 909:
      print("CONTESTAR")  
    else:
      print("Resultado: NO CONTESTAR")
  elif hour >= 17 and hour <= 19:
    if numberphone // 100000 == 877:
      print("Resultado: NO CONTESTAR")
    else:
      print("Resultado: CONTESTAR")
  elif hour >= 19:
    print("Resultado: NO CONTESTAR")
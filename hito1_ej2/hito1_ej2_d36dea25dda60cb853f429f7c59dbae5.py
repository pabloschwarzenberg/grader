#Contestador de celular
telefono = int(input(">>> Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
#verificar la hora
if 0 <= hora <= 7:
  print("CONTESTAR")
elif hora <= 14 and (str(telefono)[-1] == "9" and str(telefono)[-2] == "0" and str(telefono)[-3] == "9"):
  print("CONTESTAR")

elif 17 <= hora <= 19 and (str(telefono)[0] == "7" and str(telefono)[1] == "7" and str(telefono)[2] == "8"):
  print("CONTESTAR")
else:
  print("NO CONTESTAR")

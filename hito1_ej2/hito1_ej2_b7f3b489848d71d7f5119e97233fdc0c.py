#Contestador de celular Automaticoo

numero_telefonico1 = str(input("Ingrese numero telefonico:"))

horas = int(input("Ingrese hora de la llamada:"))

if horas > 0 and horas < 7:

  print("CONTESTAR")

if horas > 19 and horas <= 23:

  print("NO CONTESTAR")

else:

  if horas > 7 and horas < 14 and str(numero_telefonico1[-3]) == "9" and str(numero_telefonico1[-2]) == "0" and str(numero_telefonico1[-1]) == "9":

    print("CONTESTAR")

  if horas > 7 and horas < 14 and str(numero_telefonico1[-3]) != "9" and str(numero_telefonico1[-2]) != "0" and str(numero_telefonico1[-1]) != "9":

    print("NO CONTESTAR")

  if horas > 17 and horas < 19 and str(numero_telefonico1[0:1]) == "8" and str(numero_telefonico1[1:2]) == "7" and str(numero_telefonico1[2:3]) == "7":

    print("NO CONTESTAR")

  if horas > 17 and horas < 19 and str(numero_telefonico1[0:1]) != "8" and str(numero_telefonico1[1:2]) != "7" and str(numero_telefonico1[2:3]) != "7":

    print("CONTESTAR")
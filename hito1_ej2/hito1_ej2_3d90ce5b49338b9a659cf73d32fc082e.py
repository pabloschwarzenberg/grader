#Contestador de celular
numeroTelefonico = int(input("Ingrese numero telefonico: "))
horaLlamada = int(input("Ingrese hora de la llamada: "))

finNumero = (str(numeroTelefonico))[5]+(str(numeroTelefonico))[6] + (str(numeroTelefonico))[7]
iniNumero = (str(numeroTelefonico))[0]+(str(numeroTelefonico))[1] + (str(numeroTelefonico))[2]

if(horaLlamada >= 0 and horaLlamada <= 7):
    print("Resultado: Contestar")


elif (horaLlamada > 7 and horaLlamada < 14):
    if(finNumero == "909"):
         print("Resultado: Contestar")
    else:
         print("Resultado: No Contestar")

elif (horaLlamada >= 14 and horaLlamada < 17):
    print("Resultado: No Contestar")

elif (horaLlamada >= 17 and horaLlamada<= 19):
     if (iniNumero=="877"):
         print("Resultado: No Contestar")
     else:
         print("Resultado: Contestar")
else:
    print("Resultado: No Contestar")      
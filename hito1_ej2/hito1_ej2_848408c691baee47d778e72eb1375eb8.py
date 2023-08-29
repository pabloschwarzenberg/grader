#Contestador de celular

while True:
    try:
        NumeroTelefonico = int(input("Ingrese número telefonico:"))
        Hora = int(input("Ingrese hora de la llamada:"))
        if len(str(NumeroTelefonico)) > 8 or len(str(NumeroTelefonico)) < 8 or Hora < 0 or Hora > 23 :
           print("¡ERROR! Verifica tu informacion")
           continue
        break
    except:
       print("¡ERROR! Ocurrio un error, verifica la informacion")

NumeroString = str(NumeroTelefonico)

if Hora >= 0 and Hora <= 7:
    print("CONTESTAR")
    
elif (NumeroString[5] == "9" and NumeroString[6] == "0" and NumeroString[7] == "9") and (Hora > 7 and Hora <= 14):
    print("CONTESTAR")
    
elif (Hora > 7 and Hora <= 14):
    print("NO CONTESTAR")
    
elif Hora > 14 and Hora < 17:
    print("NO CONTESTAR")
    
elif (NumeroString[0] == "8" and NumeroString[1] == "7" and NumeroString[2] == "7") and (Hora >= 17 and Hora <= 19):
    print("NO CONTESTAR")
    
elif Hora >= 17 and Hora <= 19:
    print("CONTESTAR")
    
elif Hora > 19 and Hora <=23:
    print("NO CONTESTAR")      
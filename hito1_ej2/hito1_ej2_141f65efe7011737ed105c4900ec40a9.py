numeroTelefono = int(input("ingrese el numero de teléfono: "))
numeroTelefono = str(numeroTelefono)
if len(numeroTelefono)!=8:
    print ("numero equivocado")
else:
    

    primeros3 = str(numeroTelefono[0:3])
    ultimos3 = str(numeroTelefono[5:8])
    horaLlamada = int(input("Ingrese la hora de llamada de 1 a 24: "))

    if horaLlamada <= 7 or horaLlamada == 24:
        print ("contestar")

    elif horaLlamada <= 14 and ultimos3 == "909":
        print("Contestar")
    
    elif horaLlamada >= 17 and horaLlamada <= 19 and primeros3 == "877":
        print("No Contestar")

    elif horaLlamada >= 17 and horaLlamada <= 19 :
        print("Contestar")
        
    elif horaLlamada >= 19:
        print("No Contestar")
        
    else:
        horaLlamada <= 14
        print("No contestar")
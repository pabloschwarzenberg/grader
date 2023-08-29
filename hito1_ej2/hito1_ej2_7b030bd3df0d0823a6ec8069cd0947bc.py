numero_telefonico = int(input("Ingrese numero telefonico de 8 dígitos")) 

hora_llamada = int(input("Ingrese hora de la llamada entre 0 y 23")) 

numero_telefonico = str(numero_telefonico)

digitos_iniciales_3 = numero_telefonico[0] + numero_telefonico[1] + numero_telefonico[2]
digitos_finales_3 = numero_telefonico[5] + numero_telefonico[6] + numero_telefonico[7]

if(hora_llamada >= 0 and hora_llamada <= 7):
    print("CONTESTAR")

else:

    if(hora_llamada < 14):
        if(digitos_finales_3 == "909"):
            print("CONTESTAR")

        else:
            print("NO CONTESTAR")

    else:
                    
        if(hora_llamada >= 17 and hora_llamada <= 19):
            if(digitos_iniciales_3 == "877"):
                print("NO CONTESTAR")

            else:
                print("CONTESTAR")
        else:

            if(hora_llamada > 19):
                print("NO CONTESTAR")
      
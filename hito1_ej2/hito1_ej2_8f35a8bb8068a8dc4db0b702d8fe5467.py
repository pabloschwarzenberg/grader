telefono = input("Ingrese número de teléfono de 8 cifras: ")
if len(telefono)!= 8:
    print("El número de teléfono esta incorrecto")

else:
    hora = int(input("Ingrese hora del día entre 0 y 23: "))

    if not hora >= 0 or not hora <= 23:
        print("La hora esta mal ingresada")

    elif hora > 0 and hora < 7:
        print("CONTESTAR")

    elif hora >=7 and hora <14:
        if telefono[5:]=="909": 
            print ("CONTESTAR")
        else: 
            print ("NO CONTESTAR")

    elif hora >= 17 and hora <= 19:
        if telefono[:3]=="877":
            print ("NO CONTESTAR")
        else:
            print ("CONTESTAR")
            
    elif hora > 19 and hora < 23:
            print ("NO CONTESTAR")
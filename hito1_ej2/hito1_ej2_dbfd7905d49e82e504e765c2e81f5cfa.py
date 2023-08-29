Numero = int(input("Ingrese numero telefonico:"))

Hora = int(input("Ingrese hora de la llamada:"))

if Hora > -1 and Hora < 8:
    print("CONTESTAR")

elif Hora > 7 and Hora < 15 and Numero % 1000 == 909:
    print("CONTESTAR")

elif Hora > 16 and Hora < 20 and Numero % 1000 == 877:
    print("CONTESTAR")

elif Hora > 20:
    print("NO CONTESTAR")

elif Hora > 14 and Hora < 17:
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR")
        

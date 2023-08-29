#Contestador de celular
telefono= int(input("Ingrese el numero telefonico que lo esta llamando:"))
hora = int(input("Ingrese la hora que lo estan llamando:"))

digito = telefono%1000
digito2 = telefono//100000

if hora >=0 and hora <= 7:
    print("CONTESTAR")
else:
    if hora>7 and hora<14:
        if digito == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if 19>=hora>=17:
            if digito2 == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            if 19<hora<23:
                print("NO CONTESTAR")
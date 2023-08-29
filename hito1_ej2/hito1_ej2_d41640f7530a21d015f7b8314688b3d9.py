#Contestador de celular
telefono = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese la hora: "))

if telefono > 10000000 and telefono <= 99999999:
    if hora >= 0 and hora < 24:
        if hora >= 0 and hora < 8:
            print("CONTESTAR")
        if hora > 7 and hora < 15:
            if str(telefono).endswith("909"):
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
        if hora > 14 and hora < 17:
            print("NO CONTESTAR")
        if hora > 16 and hora < 20:
            if str(telefono).startswith("877"):
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        if hora > 19:
            print("NO CONTESTAR")
    else:
        print("ingrese una hora válida")
else:
    print("ingrese un numero de telefono valido (8 carácteres)")
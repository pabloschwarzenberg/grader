#Contestador de celular
telefono = int(input("Ingrese numero telefonico:"))
horallamada = int(input("Ingrese hora de la llamada"))
if 10000000 <= telefono <= 99999999 and 0 <= horallamada <= 23:
    if 0 <= horallamada <= 7:
        print("Resultado: CONTESTAR")
    if 8 <= horallamada <= 14:
        tresultimosdigitos = telefono%1000
        if tresultimosdigitos == 909:
            print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
    if 15 <= horallamada <= 16:
        print("Resultado: NO CONTESTAR")
    if 17 <= horallamada <= 19:
        tresprimerosdigitos = telefono//100000
        if tresprimerosdigitos == 877:
            print("Resultado: NO CONTESTAR")
        else:
            print("Resultado: CONTESTAR")
    if 20 <= horallamada <= 23:
        print("Resultado: NO CONTESTAR")
else:
    print("Uno o mas de los datos ingresados son invalidos.")
#Contestador de celular
telefono = int(input("Ingrese numero telefonico:"))
horallamada = int(input("Ingrese hora de la llamada:"))
if 10000000 <= telefono <= 99999999 and 0 <= horallamada <= 23:
    if 0<= horallamada <= 7:
        print("resultado: CONTESTAR")
    if 8 <= horallamada <= 14:
        tresultimosdigitos = telefono%1000
        if tresultimosdigitos == 909:
            print("resultado: CONTESTAR")
        else:
            print("resultado: NO CONTESTAR")
    if 15 <= horallamada <= 16:
        print("resultado: NO CONTESTAR")
    if 17 <= horallamada <= 19:
        tresprimerosdigitos = telefono//100000
        if tresprimerosdigitos == 877:
            print("resultado: NO CONTESTAR")
        else:
            print("resultado: CONTESTAR")
    if 20 <= horallamada <= 23:
        print("resultado: NO CONTESTAR")
else:
    print("uno o mas de los datos ingresados son invalidos:")
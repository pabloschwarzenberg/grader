#Contestador de celular
telefono = int(input("Ingrese su número de celular: "))
hora = int(input("Ingrese la hora de su llamada: "))

if telefono >= 10000000 and telefono <= 99999999:
    if hora >= 0 and hora <= 23:
        if hora >= 0 and hora <= 7:
            print("CONTESTAR")
        if hora >= 8 and hora <= 14:
            digitos3 = telefono % 1000
            if digitos3 == 909:
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
        if hora == 15 and hora == 16:
            print("NO CONTESTAR")
        if hora >= 17 and hora <= 19:
            digitoprim = telefono // 100000
            if digitoprim == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        if hora >= 20 and hora <=23:
            print("NO CONTESTAR")
    else:
        print("La hora ingresada es invalida")
else:
    print("El telefono ingresado es invalido")
#Entradas
numero = int(input("Ingrese número telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))


if numero > 99999999 or numero <= 9999999:
    print ( "número invalido")

elif hora < 0 or hora > 23:
    print("hora invalida")

else:
    if hora >= 0 and hora <= 7:
        print ("CONTESTAR")

    elif hora < 14 and (numero) % 1000:
        print ("CONTESTAR")

    elif hora < 14:
        print ("NO CONTESTAR")

    elif hora >= 17 and hora <= 19 and (numero) // 100000:
        print ("NO CONTESTAR")

    else:
        print ("NO CONTESTAR")  
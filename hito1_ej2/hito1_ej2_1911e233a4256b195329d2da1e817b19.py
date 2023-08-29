#Contestador de celular
telefono = int(input("Ingrese numero de telefono que contenga 8 cifras: "))
hora = int(input("Ingrese hora de llamada entre 0-23 hrs: "))
if (10000000 <= telefono <= 99999999) and (0 <= hora <= 23):
    if hora <= 0 and hora <= 7:
        print("CONTESTAR")

    if 8 <= hora <= 14:
        tresUltimosDigitos = telefono % 1000
        if tresUltimosDigitos == 909:
            print("CONTESTAR")

        else:
            print("NO CONTESTAR")

    if 15 <= hora <= 16:
        print("NO CONTESTAR")

    if 17 <= hora <= 19:
        tresPrimerosDigitos = telefono // 100000
        if tresPrimerosDigitos == 877:
            print("NO CONTESTAR")

        else:
            print("CONTESTAR")

    if 20 <= hora <= 23:
        print("NO CONTESTAR")

else:
    print("Uno de sus datos ingresados es invalido.")      
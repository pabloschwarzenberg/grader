#Cajero Automático
while True:
    import sys
    Usuario = eval(input("Ingrese el usuario: "))
    Clave = eval(input("Ingrese la clave: "))
    SaldoBase = 1000000
    SaldoDel_Usuario = 100000
    if Clave==1803:
        print("Clave válida")
        print("Saldo disponible: ",SaldoDel_Usuario)
    else:
        if Clave !=1803:
            print("Clave incorrecta")
            IntentoNumeroTres = int(input("Ingrese nuevamente la clave: "))
            if IntentoNumeroTres == 1803:
                print("Clave válida")
                print("Saldo disponible: ", SaldoDel_Usuario)
            else:
                print("Clave incorrecta, último intento")
                IntentoNumeroTres = int(input("Ingrese nuevamente la clave: "))
                if IntentoNumeroTres!=1803:
                    print("Tarjeta bloqueada")
                    sys.exit()
                else:
                    print("Clave válida")
                    print("Saldo disponible: ", SaldoDel_Usuario)

    Monto_a_Retirar = eval(input("Ingrese monto a retirar: "))
    if Monto_a_Retirar <= SaldoDel_Usuario:
        SaldoActual = SaldoDel_Usuario - Monto_a_Retirar
        saldocajero = SaldoBase - Monto_a_Retirar
        print("Saldo cuenta= ",SaldoActual,)
        print("Saldo cajero=",saldocajero)
    else:
        if Monto_a_Retirar > SaldoDel_Usuario:
            print("Monto no disponible")

    Exit = str(input("Ingrese cualquier digito aparte de N : "))
    if Exit != "N":
        print("Adios")
        break
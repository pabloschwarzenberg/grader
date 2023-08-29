while True:
    import sys
    us = eval(input("Ingrese el usuario: "))
    cl = eval(input("Ingrese la clave: "))
    sb = 1000000
    saldousuario = 100000
    if cl==1803:
        print("Clave válida")
        print("Saldo disponible: ",saldousuario)
    else:
        if cl !=1803:
            print("Clave incorrecta")
            intento3 = int(input("Ingrese nuevamente la clave: "))
            if intento3 == 1803:
                print("Clave válida")
                print("Saldo disponible: ", saldousuario)
            else:
                print("Clave incorrecta, último intento")
                intento3 = int(input("Ingrese nuevamente la clave: "))
                if intento3!=1803:
                    print("Tarjeta bloqueada")
                    sys.exit()
                else:
                    print("Clave válida")
                    print("Saldo disponible: ", saldousuario)

    m = eval(input("Ingrese monto a retirar: "))
    if m <= saldousuario:
        saldonuevo = saldousuario - m
        saldocajero = sb - m
        print("Saldo cuenta= ",saldonuevo,)
        print("Saldo cajero=",saldocajero)

        saldousuario=100000

        monto = m
        Billete_20000 = 0
        Billete_10000 = 0
        Billete_5000 = 0

        if monto >= 20000:
            Billete_20000 = monto // 20000
            monto = monto - (Billete_20000 * 20000)

        if monto >= 10000:
            Billete_10000 = monto // 10000
            monto = monto - (Billete_10000 * 10000)

        if monto >= 5000:
            Billete_5000 = monto // 5000
            monto = monto - (Billete_5000 * 5000)

        print("\n")
        print("billetes 20000 = {0}".format(Billete_20000))
        print("billetes 10000 = {0}".format(Billete_10000))
        print("billetes 5000 = {0}".format(Billete_5000))
    else:
        if m > saldousuario:
            print("Monto no disponible")


    let = str(input("ingrese algo distinto a N para salir: "))
    if let != "N":
        print("Hasta luego")
        break

while True:
    import sys
    usuario = eval(input("Ingrese el usuario: "))
    clave = eval(input("Ingrese la clave: "))
    salb = 1000000
    salus = 100000
    if (clave==1803):
        print("Clave válida")
        print("Saldo disponible: ",salus)
    else:
        if (clave !=1803):
            print("Clave incorrecta")
            inten3 = int(input("Ingrese nuevamente la clave: "))
            if (inten3 == 1803):
                print("Clave válida")
                print("Saldo disponible: ", salus)
            else:
                print("Clave incorrecta, último intento")
                inten3 = int(input("Ingrese nuevamente la clave: "))
                if (inten3!=1803):
                    print("Tarjeta bloqueada")
                    sys.exit()
                else:
                    print("Clave válida")
                    print("Saldo disponible: ", salus)

    monto = eval(input("Ingrese monto a retirar: "))
    if (monto <= salus):
        salnuevo = salus - monto
        salcajero = salb - monto
        print("Saldo cuenta= ",salnuevo,)
        print("Saldo cajero=",salcajero)

        salus=100000

        monto = monto 
        Billete_20000 = 0
        Billete_10000 = 0
        Billete_5000 = 0

        if (monto >= 20000):
            Billete_20000 = monto // 20000
            monto = monto - (Billete_20000 * 20000)

        if (monto >= 10000):
            Billete_10000 = monto // 10000
            monto = monto - (Billete_10000 * 10000)

        if (monto >= 5000):
            Billete_5000 = monto // 5000
            monto = monto - (Billete_5000 * 5000)

        print("\n")
        print("billetes 20000 = {0}".format(Billete_20000))
        print("billetes 10000 = {0}".format(Billete_10000))
        print("billetes 5000 = {0}".format(Billete_5000))
    else:
        if (monto > salus):
            print("Monto no disponible")


    let = str(input("ingrese algo distinto a N para salir: "))
    if let != "N":
        print("Adios")
        break
      
#Cajero Automático
while True:
    import sys
    usuario = eval(input("Ingrese el usuario: "))
    clave = eval(input("Ingrese la clave: "))
    base = 1000000
    saldo_usuario = 100000
    if clave == 1803:
        print("Clave válida")
        print("Saldo disponible: ",saldo_usuario)
    else:
        if clave != 1803:
            print("Clave incorrecta")
            intento3 = int(input("Ingrese nuevamente la clave: "))
            if intento3 == 1803:
                print("Clave válida")
                print("Saldo disponible: ", saldo_usuario)
            else:
                print("Clave incorrecta, último intento")
                intento3 = int(input("Ingrese nuevamente la clave: "))
                if intento3 != 1803:
                    print("Tarjeta bloqueada")
                    sys.exit()
                else:
                    print("Clave válida")
                    print("Saldo disponible: ", saldo_usuario)

    retiro = eval(input("Ingrese monto a retirar: "))
    if retiro <= saldo_usuario:
        saldonuevo = saldo_usuario - retiro
        saldocajero = base - retiro
        print("Saldo cuenta= ",saldonuevo)
        print("Saldo cajero=",saldocajero)

        saldo_usuario=100000

        monto = retiro
        billete_20000 = 0
        billete_10000 = 0
        billete_5000 = 0

        if monto >= 20000:
            billete_20000 = monto // 20000
            monto = monto - (billete_20000 * 20000)

        if monto >= 10000:
            billete_10000 = monto // 10000
            monto = monto - (billete_10000 * 10000)

        if monto >= 5000:
            billete_5000 = monto // 5000
            monto = monto - (billete_5000 * 5000)

        print("\n")
        print("billetes 20000 = {0}".format(billete_20000))
        print("billetes 10000 = {0}".format(billete_10000))
        print("billetes 5000 = {0}".format(billete_5000))
    else:
        if retiro > saldo_usuario:
            print("Monto no disponible")


    salir = str(input("ingrese algo distinto a N para salir: "))
    if salir != "N":
        print("Operacion finalizada con exito")
        break
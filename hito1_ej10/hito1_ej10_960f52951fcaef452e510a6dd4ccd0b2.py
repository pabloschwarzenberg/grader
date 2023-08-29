while True:
    import sys
    x = eval(input("Ingrese el usuario: "))
    y = eval(input("Ingrese la clave: "))
    z = 1000000
    saldo = 100000
    if y==1803:
        print("Clave válida")
        print("Saldo disponible: ",saldo)
    else:
        if y !=1803:
            print("Clave incorrecta")
            intento3 = int(input("Ingrese nuevamente la clave: "))
            if intento3 == 1803:
                print("Clave válida")
                print("Saldo disponible: ", saldo)
            else:
                print("Clave incorrecta, último intento")
                intento3 = int(input("Ingrese nuevamente la clave: "))
                if intento3 != 1803:
                    print("Tarjeta bloqueada")
                    sys.exit()
                else:
                    print("Clave válida")
                    print("Saldo disponible: ", saldo)

    c = eval(input("Ingrese monto a retirar: "))
    if c <= saldo:
        saldonuevo = saldo - c
        saldocajero = z - c
        print("Saldo cuenta= ",saldonuevo,)
        print("Saldo cajero=",saldocajero)
    else:
        if c > saldo:
            print("Monto no disponible")

    let = str(input("ingrese algo distinto a N para salir: "))
    if let != "N":
        print("Hasta luego")
        break

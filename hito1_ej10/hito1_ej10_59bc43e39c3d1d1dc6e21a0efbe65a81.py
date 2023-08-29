#Cajero Automático
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
    else:
        if m > saldousuario:
            print("Monto no disponible")

    let = str(input("ingrese algo distinto a N para salir: "))
    if let != "N":
        print("Hasta luego")
        break

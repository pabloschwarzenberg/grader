#Cajero Automático
while True:
    import sys
    usuario = eval(input("Ingrese el usuario: "))
    clave = eval(input("Ingrese la clave: "))
    salb = 1000000
    salus = 100000
    if clave==1803:
        print("Clave válida")
        print("Saldo disponible: ",salus)
    else:
        if clave !=1803:
            print("Clave incorrecta")
            inte3 = int(input("Ingrese nuevamente la clave: "))
            if inte3 == 1803:
                print("Clave válida")
                print("Saldo disponible: ", salus)
            else:
                print("Clave incorrecta, último intento")
                inte3 = int(input("Ingrese nuevamente la clave: "))
                if inte3!=1803:
                    print("Tarjeta bloqueada")
                    sys.exit()
                else:
                    print("Clave válida")
                    print("Saldo disponible: ", salus)

    monto = eval(input("Ingrese monto a retirar: "))
    if monto <= salus:
        salnew = salus - monto
        salcajero = salb - monto
        print("Saldo cuenta= ",salnew,)
        print("Saldo cajero=",salcajero)
    else:
        if monto > salus:
            print("Monto no permitido")

    let = str(input("ingrese algo distinto a N para salir: "))
    if let != "N":
        print("Adios")
        break
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
# al principio el saldo de 1.000.000 estará distribuido en 20 billetes de 20.000, 40 billetes de 10.000 y 40 billetes de 5.000
    Monto_a_Retirar = eval(input("Ingrese monto a retirar: "))
    if Monto_a_Retirar <= SaldoDel_Usuario:
        SaldoActual = SaldoDel_Usuario - Monto_a_Retirar
        saldocajero = SaldoBase - Monto_a_Retirar
        cant20000 = Monto_a_Retirar // 20000
        resto20000 = Monto_a_Retirar % 20000

        cant10000 = resto20000 // 10000
        resto10000 = resto20000 % 10000

        cant5000 = resto10000 // 5000
        resto5000 = resto10000 % 5000

        print("Saldo cuenta= ",SaldoActual)
        print("Saldo cajero=",saldocajero)
        print("billetes 20000 =", cant20000)
        print("billetes 10000 =", cant10000)
        print("billetes 5000 =", cant5000)
    else:
        if Monto_a_Retirar > SaldoDel_Usuario:
            print("Monto no disponible")

    Exit = str(input("Ingrese cualquier digito aparte de N : "))
    if Exit != "N":
        print("Adios")
        break
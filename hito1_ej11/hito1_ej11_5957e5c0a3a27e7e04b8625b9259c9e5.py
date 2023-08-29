
SalInicial = 1000000
SalCuenta = 100000

Usuario = int(input("ingrece usuario:"))
Clave = int(input("ingrece su clave:"))

while Usuario == 10334151:
    if Usuario == 10334151 and Clave == 1803:
        Monto = int(input("monto a retirar: "))
        if 0 > Monto > SalInicial:
            print("monto no valido")

        elif 1 <= Monto <= SalInicial:
            billetes = [20000, 10000, 5000]
            resto = Monto

            for billetes in billetes:
                Sald = resto // billetes
                if Sald > 0:
                    if Sald == 0:
                        print("billetes", billetes, "=", Sald)

                    else:
                        print("billetes", billetes, "=", Sald)
                    resto %= billetes

            print("saldo cuenta =", SalCuenta - Monto)
            print("saldo cajero =", SalInicial - Monto)

            break

    Usuario = int(input("ingrece usuario: "))
    Clave = int(input("ingrece su clave: "))

    if Usuario == 10334151 and Clave == 1803:
        Monto = int(input("monto a retirar: "))

        if 0 > Monto > SalInicial:
            print("monto no valido")

        elif 1 <= Monto <= SalInicial:
            billetes = [20000, 10000, 5000]
            resto = Monto

            for billetes in billetes:
                Sald = resto // billetes

                if Sald > 0:
                    if Sald == 0:
                        print("billetes", billetes, "=", Sald)

                    else:
                        print("billetes", billetes, "=", Sald)
                    resto %= billetes

            print("saldo cuenta =", SalCuenta - Monto)
            print("saldo cajero =", SalInicial - Monto)
            break

    Usuario = int(input("ingrece usuario: "))
    Clave = int(input("ingrece su clave: "))

    if Usuario == 10334151 and Clave == 1803:
        Mont2 = int(input("monto a retirar: "))

        if 0 > Mont2 > SalInicial:
            print("monto no valido")

        elif 1 <= Mont2 <= SalInicial:
            billetes = [20000, 10000, 5000]
            resto = Mont2

            for billetes in billetes:
                Sald = resto // billetes

                if Sald > 0:
                    if Sald == 0:
                        print("billetes", billetes, "=", Sald)

                    else:
                        print("billetes", billetes, "=", Sald)
                    resto %= billetes

            print("saldo cuenta =", SalCuenta - Mont2)
            print("saldo cajero =", SalInicial - Mont2)
            break

    Inval = 0
    Usuario = 1

    while not (Usuario == 0):
        if (Usuario != 10334151 and Clave != 1803) or (Usuario != 10334151 and Clave == 1803) or (Usuario == 10334151 and Clave != 1803):
            Inval = Inval + 1
            if Inval <= 2:
                print("Clave invalida")
                Usuario = int(input("ingrece usuario: "))
                Seg = int(input("ingrece clave: "))

            else:
                print("Tarejeta Bloqueada")
                break

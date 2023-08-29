SalInicial = 1000000
SalCuenta = 100000


Usuario = int(input("Ingrece usuario: "))
Clave = int(input("Ingrece clave: "))


while Usuario == 10334151:

    if Usuario == 10334151 and Clave == 1803:
        Monto = int(input("Monto a retirar: "))
        if 0 > Monto > SalInicial:
            print("Monto no valido")

        elif 1 <= Monto <= SalInicial:
            print("Saldo cuenta =", SalCuenta - Monto)
            print("Saldo cajero =", SalInicial - Monto)

            break

    Usuario = int(input("Ingrece usuario: "))
    Clave = int(input("Ingrece clave: "))

    if Usuario == 10334151 and Clave == 1803:
        Mont2 = int(input("Monto a retirar: "))
        if 0 > Mont2 > SalInicial:
            print("Monto no valido")

        elif 1 <= Mont2 <= SalInicial:
            print("Saldo cuenta=", SalCuenta - Mont2)
            print("Saldo cajero=", SalInicial - Mont2)
            break

    Usuario = int(input("Ingrece usuario: "))
    Clave = int(input("Ingrece clave: "))

    if Usuario == 10334151 and Clave == 1803:
        Mont2 = int(input("Monto a retirar: "))
        if 0 > Mont2 > SalInicial:
            print("Monto no valido")

        elif 1 <= Mont2 <= SalInicial:
            print("Saldo cuenta=", SalCuenta - Mont2)
            print("Saldo cajero=", SalInicial - Mont2)

            break
    Inva = 0
    Usuario = 1
    while not (Usuario == 0):
        if (Usuario != 10334151 and Clave != 1803) or (Usuario != 10334151 and Clave == 1803) or (Usuario == 10334151 and Clave != 1803):
            Inva = Inva + 1
            if Inva <= 2:
                print("Clave invalida")
                Usuario = int(input("ingrece usuario: "))
                Clave = int(input("ingrece clave: "))


            else:
                print("Tarejeta Bloqueada")
                break

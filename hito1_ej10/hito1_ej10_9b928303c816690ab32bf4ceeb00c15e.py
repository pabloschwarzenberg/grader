A = 1000000
B = 100000


C = int(input("Ingrece usuario: "))
D = int(input("Ingrece clave: "))


while C == 10334151:

    if C == 10334151 and D == 1803:
        E = int(input("Monto a retirar: "))
        if 0 > E > A:
            print("Monto no valido")

        elif 1 <= E <= A:
            print("Saldo cuenta =", B - E)
            print("Saldo cajero =", A - E)

            break

    C = int(input("Ingrece usuario: "))
    D = int(input("Ingrece clave: "))

    if C == 10334151 and D == 1803:
        F = int(input("Monto a retirar: "))
        if 0 > F > A:
            print("Monto no valido")

        elif 1 <= F <= A:
            print("Saldo cuenta=", B - F)
            print("Saldo cajero=", A - F)
            break

    C = int(input("Ingrece usuario: "))
    D = int(input("Ingrece clave: "))

    if C == 10334151 and D == 1803:
        F = int(input("Monto a retirar: "))
        if 0 > F > A:
            print("Monto no valido")

        elif 1 <= F <= A:
            print("Saldo cuenta=", B - F)
            print("Saldo cajero=", A - F)

            break
    Z = 0
    C = 1
    while not (C == 0):
        if (C != 10334151 and D != 1803) or (C != 10334151 and D == 1803) or (C == 10334151 and D != 1803):
            Z = Z+1
            if Z <= 2:
                print("Clave invalida")
                C = int(input("ingrece usuario: "))
                D = int(input("ingrece clave: "))


            else:
                print("Tarejeta Bloqueada")
                break




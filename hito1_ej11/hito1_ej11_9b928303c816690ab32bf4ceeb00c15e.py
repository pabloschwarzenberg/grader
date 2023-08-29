#Cajero Automático
A = 1000000
B = 100000


C = int(input("ingrece usuario:"))
D = int(input("ingrece su clave:"))


while C == 10334151:
    if C == 10334151 and D == 1803:
        E = int(input("monto a retirar: "))
        if 0 > E > A:
            print("monto no valido")

        elif 1 <= E <= A:
            billetes = [20000, 10000, 5000]
            resto = E

            for billetes in billetes:
                b = resto // billetes
                if b > 0:
                    if b == 0:
                        print("billetes", billetes, "=", b)

                    else:
                        print("billetes", billetes, "=", b)
                    resto %= billetes

            print("saldo cuenta =", B - E)
            print("saldo cajero =", A - E)

            break

    C = int(input("ingrece usuario: "))
    D = int(input("ingrece su clave: "))

    if C == 10334151 and D == 1803:
        F = int(input("monto a retirar: "))

        if 0 > F > A:
            print("monto no valido")

        elif 1 <= F <= A:
            billetes = [20000, 10000, 5000]
            resto = F

            for billetes in billetes:
                b = resto // billetes

                if b > 0:
                    if b == 0:
                        print("billetes", billetes, "=", b)

                    else:
                        print("billetes", billetes, "=", b)
                    resto %= billetes

            print("saldo cuenta =", B - F)
            print("saldo cajero =", A - F)
            break

    C = int(input("ingrece usuario: "))
    D = int(input("ingrece su clave: "))

    if C == 10334151 and D == 1803:
        G = int(input("monto a retirar: "))

        if 0 > G > A:
            print("monto no valido")

        elif 1 <= G <= A:
            billetes = [20000, 10000, 5000]
            resto = G

            for billetes in billetes:
                b = resto // billetes

                if b > 0:
                    if b == 0:
                        print("billetes", billetes, "=", b)

                    else:
                        print("billetes", billetes, "=", b)
                    resto %= billetes

            print("saldo cuenta =", B - G)
            print("saldo cajero =", A - G)
            break

    Z = 0
    C = 1
    
    while not (C == 0):
        if (C != 10334151 and D != 1803) or (C != 10334151 and D == 1803) or (C == 10334151 and D != 1803):
            Z = Z + 1
            if Z <= 2:
                print("Clave invalida")
                C = int(input("ingrece usuario: "))
                D = int(input("ingrece clave: "))
                
            else:
                print("Tarejeta Bloqueada")
                break


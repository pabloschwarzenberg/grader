#Cajero Automático
inicial = 1000000
saldo = 100000
us = int(input("ingrece usuario:"))
clave = int(input("ingrece su clave:"))
while us == 10334151:
    if us == 10334151 and clave == 1803:
        x = int(input("monto a retirar:"))
        if 0 > x > inicial:
            print("monto no valido")
        elif 1 <= x <= inicial:
            billetes = [20000, 10000, 5000]
            resto = x
            for billetes in billetes:
                b = resto // billetes
                if b > 0:
                    if b == 0:
                        print("billetes", billetes, "=", b)
                    else:
                        print("billetes", billetes, "=", b)
                    resto %= billetes
            print("saldo cuenta=", saldo - x)
            print("saldo cajero=", inicial - x)

            break

    us = int(input("ingrece usuario:"))
    clave = int(input("ingrece su clave:"))
    if us == 10334151 and clave == 1803:
        x = int(input("monto a retirar:"))
        if 0 > x > inicial:
            print("monto no valido")
        elif 1 <= x <= inicial:
            billetes = [20000, 10000, 5000]
            resto = x
            for billetes in billetes:
                b = resto // billetes
                if b > 0:
                    if b == 0:
                        print("billetes", billetes, "=", b)
                    else:
                        print("billetes", billetes, "=", b)
                    resto %= billetes

            print("saldo cuenta=", saldo - x)
            print("saldo cajero=", inicial - x)
            break

    us = int(input("ingrece usuario:"))
    clave = int(input("ingrece su clave:"))
    if us == 10334151 and clave == 1803:
        x = int(input("monto a retirar:"))
        if 0 > x > inicial:
            print("monto no valido")
        elif 1 <= x <= inicial:
            billetes = [20000, 10000, 5000]
            resto = x
            for billetes in billetes:
                b = resto // billetes
                if b > 0:
                    if b == 0:
                        print("billetes", billetes, "=", b)
                    else:
                        print("billetes", billetes, "=", b)
                    resto %= billetes
            print("saldo cuenta=", saldo - x)
            print("saldo cajero=", inicial - x)
            break
    elif us == 10334151 and clave != 1803:
        print("tarjeta bloqueada")

        break      
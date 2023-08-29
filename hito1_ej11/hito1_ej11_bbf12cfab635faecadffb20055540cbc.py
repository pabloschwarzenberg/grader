saldo = 1000000
saldoC = 100000
usuario= int(input("Ingrese el Número de Usuario: "))
clave = int(input("Ingrese la clave: "))
intentos = 0
Billetes_20mil = 20
Billetes_10mil = 40
Billetes_5mil = 40


while usuario == 10334151:
    try:
        if clave != 1803:
            intentos = intentos +1
            print("clave invalida")
            clave = int(input("Ingrese la clave: "))
            if intentos == 2 and clave != 1809:
                print("tarjeta bloqueada")
                break
        else:
            if clave == 1803:
                plata = int(input("Ingrese el monto a retirar: "))
                if plata > 5000:
                    x = plata // 20000
                    print("billetes 20000=", x)
                    if plata - (20000 * x) < 20000:
                        y = plata - (20000 * x)
                        z = y // 10000
                        print("billetes 10000=", z)
                        if plata - ((20000 * x)+(10000 * z))< plata:
                            n = plata - ((20000 * x)+(10000 * z))
                            e = n//5000
                            dinero = saldoC - plata
                            pcajero = saldo - plata
                            print("billetes 5000=",e)
                            print(Billetes_20mil - x)
                            print(Billetes_10mil - z)
                            print(Billetes_5mil - e)
                            print("saldo cuenta=",dinero)
                            print("saldo cajero=", pcajero)
                if plata == 5000:
                    print("billetes 20000= 0")
                    print("billetes 10000= 0")
                    print("billetes 5000== 1")
                    print(Billetes_20mil)
                    print(Billetes_10mil)
                    print(Billetes_5mil - 1)
                if plata > 100000:
                    print("Monto no permitido")
                    continue

    except ValueError:
        break




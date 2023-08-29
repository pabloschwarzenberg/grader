#Cajero Automático
def cajero():
    saldo_cajero = 1000000
    saldo_cuenta = 100000
    intentos = 0

    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40

    while True:
        usuario_valido = 10334151
        clave_valida = 1803

        usuario = int(input("Ingrese su usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            while True:
                monto = int(input("Ingrese el monto a retirar: "))

                if monto > saldo_cuenta:
                    print("Monto no permitido.")
                else:
                    if monto > (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
                        print("No hay suficientes billetes disponibles.")
                    else:
                        billetes_20000_entregados = min(monto // 20000, billetes_20000)
                        monto -= billetes_20000_entregados * 20000

                        billetes_10000_entregados = min(monto // 10000, billetes_10000)
                        monto -= billetes_10000_entregados * 10000

                        billetes_5000_entregados = min(monto // 5000, billetes_5000)
                        monto -= billetes_5000_entregados * 5000

                        saldo_cuenta -= (billetes_20000_entregados * 20000 + billetes_10000_entregados * 10000 + billetes_5000_entregados * 5000)
                        saldo_cajero = saldo_cajero - saldo_cuenta

                        billetes_20000 -= billetes_20000_entregados
                        billetes_10000 -= billetes_10000_entregados
                        billetes_5000 -= billetes_5000_entregados

                        print("Saldo cuenta =", saldo_cuenta)
                        print("Saldo cajero =", saldo_cajero)
                        print("Billetes 20000 =", billetes_20000_entregados)
                        print("Billetes 10000 =", billetes_10000_entregados)
                        print("Billetes 5000 =", billetes_5000_entregados)

                continuar = input("¿Desea realizar otra transacción? (N para salir): ")
                if continuar.upper() == "N":
                    break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada.", intentos, "de 3")
                break
            else:
                print("Clave inválida.", intentos, "de 3")

cajero()
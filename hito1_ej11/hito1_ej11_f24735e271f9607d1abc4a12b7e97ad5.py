#Cajero Automático
saldo_cajero = 1000000
saldo_usuario = 100000

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

max_intentos_fallidos = 3
intentos_fallidos = 0

usuario_permitido = 10334151
clave_permitida = 1803

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario != usuario_permitido or clave != clave_permitida:
        print("Clave inválida")
        intentos_fallidos += 1

        if intentos_fallidos >= max_intentos_fallidos:
            print("Tarjeta bloqueada")
            break
    else:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= 0 or monto_retiro > saldo_usuario:
            print("Monto no permitido")
        else:
            if monto_retiro > saldo_cajero:
                print("No hay suficiente dinero en el cajero")
            else:
                # Cálculo de la cantidad de billetes para cada denominación
                billetes_20000_retirados = min(billetes_20000, int(monto_retiro / 20000))
                monto_retiro -= billetes_20000_retirados * 20000
                billetes_10000_retirados = min(billetes_10000, int(monto_retiro / 10000))
                monto_retiro -= billetes_10000_retirados * 10000
                billetes_5000_retirados = min(billetes_5000, int(monto_retiro / 5000))
                monto_retiro -= billetes_5000_retirados * 5000

                # Actualización de los saldos y billetes disponibles
                saldo_usuario -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
                saldo_cajero -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
                billetes_20000 -= billetes_20000_retirados
                billetes_10000 -= billetes_10000_retirados
                billetes_5000 -= billetes_5000_retirados

                # Impresión de la cantidad de billetes entregados
                print("Billetes 20000 =", billetes_20000_retirados)
                print("Billetes 10000 =", billetes_10000_retirados)
                print("Billetes 5000 =", billetes_5000_retirados)

                print("Saldo cuenta =", saldo_usuario)
                print("Saldo cajero =", saldo_cajero)
                break     
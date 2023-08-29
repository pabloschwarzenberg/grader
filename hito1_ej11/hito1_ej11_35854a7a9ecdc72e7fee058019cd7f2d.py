saldo_cuenta_corriente = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

usuario = "10334151"
clave = "1803"

while True:
    ingreso_usuario = input("Ingrese su usuario: ")
    ingreso_clave = input("Ingrese su clave: ")

    if ingreso_usuario == usuario and ingreso_clave == clave:
        while True:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro <= 0:
                print("Monto no permitido")
            elif monto_retiro > saldo_cuenta_corriente:
                print("Saldo insuficiente")
            elif monto_retiro > saldo_cajero:
                print("Cajero sin suficiente efectivo")
            else:
                # Distribución de billetes
                billetes_20000_retirados = min(monto_retiro // 20000, billetes_20000)
                monto_retiro -= billetes_20000_retirados * 20000

                billetes_10000_retirados = min(monto_retiro // 10000, billetes_10000)
                monto_retiro -= billetes_10000_retirados * 10000

                billetes_5000_retirados = min(monto_retiro // 5000, billetes_5000)
                monto_retiro -= billetes_5000_retirados * 5000

                if monto_retiro > 0:
                    print("Monto no permitido")
                else:
                    # Actualización de saldos
                    saldo_cuenta_corriente -= (billetes_20000_retirados * 20000 +
                                               billetes_10000_retirados * 10000 +
                                               billetes_5000_retirados * 5000)
                    saldo_cajero -= (billetes_20000_retirados * 20000 +
                                     billetes_10000_retirados * 10000 +
                                     billetes_5000_retirados * 5000)

                    print("Retiro exitoso")
                    print("Saldo cuenta: " + str(saldo_cuenta_corriente))
                    print("Saldo cajero: " + str(saldo_cajero))
                    print("Billetes de 20.000: " + str(billetes_20000_retirados))
                    print("Billetes de 10.000: " + str(billetes_10000_retirados))
                    print("Billetes de 5.000: " + str(billetes_5000_retirados))
                break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break
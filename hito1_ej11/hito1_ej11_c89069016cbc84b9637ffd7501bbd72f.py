#Cajero Automático
def cajero():
    usuario = 10334151
    clave = 1803
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40
    intentos = 0

    while True:
        ingreso_usuario = int(input("Ingrese su usuario: "))
        ingreso_clave = int(input("Ingrese su clave: "))

        if ingreso_usuario == usuario and ingreso_clave == clave:
            while True:
                monto = int(input("Ingrese el monto a retirar: "))

                if monto <= saldo_cuenta:
                    if monto <= saldo_cajero:
                        if monto % 5000 == 0:
                            if monto <= (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
                                billetes_20000_retirados = min(monto // 20000, billetes_20000)
                                monto -= billetes_20000_retirados * 20000
                                billetes_10000_retirados = min(monto // 10000, billetes_10000)
                                monto -= billetes_10000_retirados * 10000
                                billetes_5000_retirados = min(monto // 5000, billetes_5000)
                                monto -= billetes_5000_retirados * 5000

                                saldo_cuenta -= (billetes_20000_retirados * 20000 +
                                                 billetes_10000_retirados * 10000 +
                                                 billetes_5000_retirados * 5000)
                                saldo_cajero -= (billetes_20000_retirados * 20000 +
                                                 billetes_10000_retirados * 10000 +
                                                 billetes_5000_retirados * 5000)

                                print("Retiro exitoso.")
                                print("Saldo cuenta:", saldo_cuenta)
                                print("Saldo cajero:", saldo_cajero)
                                print("Billetes 20000:", billetes_20000_retirados)
                                print("Billetes 10000:", billetes_10000_retirados)
                                print("Billetes 5000:", billetes_5000_retirados)
                            else:
                                print("Monto no permitido. Saldo insuficiente de billetes en el cajero.")
                        else:
                            print("Monto no permitido. Solo se pueden retirar múltiplos de 5000.")
                    else:
                        print("Monto no permitido. Saldo insuficiente en el cajero.")
                else:
                    print("Monto no permitido. Saldo insuficiente en la cuenta.")

                opcion = input("¿Desea realizar otro retiro? (S/N): ")
                if opcion != "S":
                    break
        else:
            intentos += 1
            print("Clave inválida.")

        if intentos >= 3:
            print("Tarjeta bloqueada.")
            break

        opcion = input("¿Desea salir? (S/N): ")
        if opcion != "N":
            break

cajero()

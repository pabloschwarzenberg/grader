#Cajero Automático
def cajero():
    saldo_cuenta = 100000
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }
    intentos_fallidos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            print("¡Bienvenido!")
            saldo_cuenta = 100000
            intentos_fallidos = 0
            break
        else:
            intentos_fallidos += 1
            print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0 or monto > saldo_cuenta:
            print("Monto no permitido.")
        else:
            billetes_retirados = {
                20000: 0,
                10000: 0,
                5000: 0
            }

            for billete, cantidad in saldo_cajero.items():
                if monto >= billete and cantidad > 0:
                    num_billetes = min(monto // billete, cantidad)
                    billetes_retirados[billete] = num_billetes
                    monto -= billete * num_billetes
                    saldo_cajero[billete] -= num_billetes

            if monto == 0:
                saldo_cuenta -= (billetes_retirados[20000] * 20000
                                 + billetes_retirados[10000] * 10000
                                 + billetes_retirados[5000] * 5000)
                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                print("Billetes entregados:")
                for billete, cantidad in billetes_retirados.items():
                    if cantidad > 0:
                        print("billetes", billete, "=", cantidad)
            else:
                print("Monto no permitido.")

        opcion = input("¿Desea realizar otro retiro? (S/N): ")

        if opcion.upper() != "S":
            break

cajero()      
#Cajero Automático
def cajero():
    saldo_cuenta = 100000
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            saldo_cuenta_usuario = saldo_cuenta
            intentos = 0
            break
        else:
            print("Usuario o clave incorrectos.")
            intentos += 1

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_cuenta_usuario:
            print("Saldo insuficiente.")
        elif monto > sum(billete * cantidad for billete, cantidad in saldo_cajero.items()):
            print("El cajero no tiene suficiente dinero para realizar el retiro.")
        else:
            billetes_entregados = {}
            saldo_billetes = sum(billete * cantidad for billete, cantidad in saldo_cajero.items())
            if monto % 5000 != 0 or monto > saldo_billetes:
                print("No es posible entregar el monto solicitado con los billetes disponibles.")
            else:
                for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
                    if monto >= billete:
                        num_billetes = min(monto // billete, cantidad)
                        billetes_entregados[billete] = num_billetes
                        monto -= billete * num_billetes

                saldo_cuenta_usuario -= sum(billete * cantidad for billete, cantidad in billetes_entregados.items())
                saldo_cajero = {billete: cantidad - billetes_entregados.get(billete, 0) for billete, cantidad in saldo_cajero.items()}

                print("Saldo cuenta =", saldo_cuenta_usuario)
                print("Saldo cajero =", sum(billete * cantidad for billete, cantidad in saldo_cajero.items()))
                print("Suma de billetes =", int(sum(billete * cantidad for billete, cantidad in billetes_entregados.items())))
                for billete, cantidad in billetes_entregados.items():
                    print("Billetes", billete, "=", cantidad)
                break

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()

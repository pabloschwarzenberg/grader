def cajero():
    usuario_valido = 10334151
    clave_valida = 1803
    saldo_inicial = 100000
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    intentos = 0

    while intentos < 3:
        usuario = int(input("Ingrese su número de usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro > saldo_inicial:
                print("Monto no permitido. Saldo insuficiente.")
            elif monto_retiro > sum(saldo_cajero.values()) * min(saldo_cajero.keys()):
                print("Monto no permitido. Saldo insuficiente en el cajero.")
            else:
                billetes_entregados = {}

                for denominacion, cantidad in saldo_cajero.items():
                    billetes_necesarios = monto_retiro // denominacion
                    billetes_a_entregar = min(billetes_necesarios, cantidad)

                    if billetes_a_entregar > 0:
                        billetes_entregados[denominacion] = billetes_a_entregar
                        monto_retiro -= billetes_a_entregar * denominacion
                        saldo_cajero[denominacion] -= billetes_a_entregar

                saldo_inicial -= monto_retiro

                print("Retiro exitoso.")
                print("Nuevo saldo en la cuenta corriente: ", saldo_inicial)
                print(billetes_a_entregar)
                for denominacion, cantidad in billetes_entregados.items():
                    print("Billetes", denominacion, "=", cantidad)
                print("Nuevo saldo en el cajero: ", sum(saldo_cajero.values()) * min(saldo_cajero.keys()))
                break
        else:
            print("Clave inválida.")
            intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada.")


# Ejemplo de uso
cajero()

def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese el usuario: ")
        clave = input("Ingrese la clave: ")

        if usuario == "10334151" and clave == "1803":
            saldo_disponible = saldo_cuenta
            intentos = 0

            while True:
                monto = float(input("Ingrese el monto a retirar: "))

                if monto > saldo_disponible:
                    print("Monto no permitido. El saldo disponible es:", saldo_disponible)
                else:
                    saldo_cuenta -= monto
                    saldo_cajero -= monto
                    print("Retiro exitoso.")
                    print("Saldo cuenta:", saldo_cuenta)
                    print("Saldo cajero:", saldo_cajero)

                continuar = input("¿Desea realizar otro retiro? (S/N): ")

                if continuar.upper() != "S":
                    break

        else:
            intentos += 1
            print("Clave inválida.")
            if intentos == 3:
                print("Tarjeta bloqueada.")
                break


cajero()

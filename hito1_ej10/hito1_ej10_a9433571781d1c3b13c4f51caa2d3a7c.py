saldo_inicial_cuenta = 1000000
saldo_inicial_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        saldo_cuenta = saldo_inicial_cuenta
        saldo_cajero = saldo_inicial_cajero

        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_cuenta:
                if monto_retiro <= saldo_cajero:
                    saldo_cuenta -= monto_retiro
                    saldo_cajero -= monto_retiro

                    print("Retiro exitoso.")
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", saldo_cajero)
                else:
                    print("Monto no permitido. No hay suficiente dinero en el cajero.")
            else:
                print("Monto no permitido. No hay suficiente dinero en la cuenta.")

            continuar = input("¿Desea realizar otro retiro? (S/N): ")
            if continuar.upper() != "S":
                break

        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break
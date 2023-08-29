def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            saldo_usuario = saldo_cuenta
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada")
                return

    while True:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_usuario:
            if monto_retiro <= saldo_cajero:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
            else:
                print("Monto no permitido: no hay suficiente dinero en el cajero")
        else:
            print("Monto no permitido: no hay suficiente saldo en la cuenta")

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()
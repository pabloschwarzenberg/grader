def cajero():
    saldo_cajero = 1000000
    saldo_cuenta = 100000
    intentos = 0

    usuario_valido = 10334151
    clave_valida = 1803

    while True:
        usuario = int(input("Ingrese su número de usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            print("Inicio de sesión exitoso.")
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada. Demasiados intentos fallidos.")
                return
            print("Clave inválida. Intente nuevamente.")

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido. No tiene suficiente saldo en su cuenta.")
        elif monto > saldo_cajero:
            print("Monto no permitido. El cajero no dispone de suficiente dinero.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo en cuenta:", saldo_cuenta)
            print("Saldo en cajero:", saldo_cajero)

        continuar = input("¿Desea realizar otra transacción? (S/N): ")
        if continuar != "S":
            break

cajero()

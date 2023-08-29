def cajero():
    saldo_cajero = 1000000
    saldo_usuario = 100000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            print("Bienvenido, usuario.")
            break
        else:
            intentos += 1
            print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada. Por favor, contacte al banco.")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_usuario:
            print("Saldo insuficiente.")
        elif monto > saldo_cajero:
            print("El cajero no tiene suficiente dinero para realizar la transacción.")
        else:
            saldo_usuario -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta={:.1f}".format(saldo_usuario))
            print("Saldo cajero={:.1f}".format(saldo_cajero))

        continuar = input("¿Desea realizar otra transacción? (S/N): ")
        if continuar.upper() != "S":
            break

cajero()
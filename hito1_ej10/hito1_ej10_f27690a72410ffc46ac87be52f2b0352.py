def cajero_automatico():
    saldo_inicial = 1000000
    saldo_cuenta = 100000
    saldo_cajero = saldo_inicial

    intentos = 0
    usuario_valido = False

    while not usuario_valido and intentos < 3:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            usuario_valido = True
        else:
            print("Clave inválida.")
            intentos += 1

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        if saldo_cuenta == 0:
            print("Saldo insuficiente en la cuenta.")
            return

        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso.")
            print("Saldo cuenta=" + str(saldo_cuenta))
            print("Saldo cajero=" + str(saldo_cajero))
        elif monto_retiro > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")
        elif monto_retiro > saldo_cajero:
            print("Monto no permitido. Saldo insuficiente en el cajero.")

        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion.upper() != "S":
            break

cajero_automatico()

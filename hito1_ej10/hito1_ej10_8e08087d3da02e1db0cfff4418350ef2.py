def cajero():
    saldo_inicial = 1000000
    saldo_cuenta = 100000
    saldo_cajero = saldo_inicial

    usuario_valido = False
    clave_valida = False
    intentos_fallidos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            usuario_valido = True
            break
        else:
            intentos_fallidos += 1
            print("Clave inválida.")

        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        monto = input("Ingrese el monto a retirar: ")

        if not monto.isdigit():
            print("Monto no válido.")
            continue

        monto = int(monto)

        if monto <= saldo_cuenta:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
        else:
            print("Monto no permitido.")

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break


cajero()
      
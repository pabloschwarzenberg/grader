saldo_cuenta = 1000000  # Saldo inicial de la cuenta
saldo_cajero = 1000000  # Saldo inicial del cajero
intentos_fallidos = 0  # Contador de intentos fallidos

while True:
    # Pedir usuario y clave
    try:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
    except EOFError:
        print("Error: Entrada finalizada de forma inesperada.")
        break

    # Verificar usuario y clave
    if usuario == "10334151" and clave == "1803":
        saldo_usuario = 100000  # Saldo del usuario autenticado
        intentos_fallidos = 0  # Reiniciar contador de intentos fallidos

        # Pedir monto a retirar
        try:
            monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Error: Entrada inválida para el monto.")
            continue

        # Validar monto a retirar
        if monto <= saldo_usuario:
            if monto <= saldo_cajero:
                saldo_usuario -= monto
                saldo_cajero -= monto
                print("Retiro exitoso")
                print("Saldo cuenta =", saldo_usuario)
                print("Saldo cajero =", saldo_cajero)
            else:
                print("Monto no permitido. Fondos insuficientes en el cajero.")
        else:
            print("Monto no permitido. Fondos insuficientes en la cuenta.")

    else:
        intentos_fallidos += 1
        print("Clave inválida")

        # Verificar si se superó el límite de intentos fallidos
        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada. Contacte al servicio al cliente.")
            break

    opcion = input("¿Desea realizar otra transacción? (N para salir): ")
    if opcion.upper() == "N":
        break

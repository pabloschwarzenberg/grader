def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 3

    print("¡Bienvenido al cajero automático!")
    print("Ingrese su usuario y contraseña para acceder.")

    while intentos > 0:
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        if usuario == "10334151" and clave == "1803":
            print("Acceso concedido.")
            break
        else:
            print("Clave inválida.")
            intentos -= 1

            if intentos == 0:
                print("Tarjeta bloqueada.")
                return

    while True:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta:
            if monto_retiro <= saldo_cajero:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Saldo cuenta=",saldo_cuenta)
                print("Saldo cajero=",saldo_cajero)
            else:
                print("Monto no permitido. El cajero no cuenta con suficiente saldo.")
        else:
            print("Monto no permitido. No tienes suficiente saldo en tu cuenta.")

        opcion = input("\n¿Desea realizar otra transacción? (S/N): ")
        if opcion.upper() != "S":
            break

# Ejecutar el cajero
cajero()

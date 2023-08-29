saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= saldo_cuenta:
                saldo_cuenta -= monto
                saldo_cajero -= monto

                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)

                break
            else:
                print("Monto no permitido. El saldo actual de la cuenta es", saldo_cuenta)
    else:
        intentos_fallidos += 1
        print("Clave inválida. Intentos fallidos:", intentos_fallidos)

        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada.")
            break

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break
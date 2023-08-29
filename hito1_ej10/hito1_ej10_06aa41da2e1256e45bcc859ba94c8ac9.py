#Cajero Automático
def cajero():
    saldo_cajero = 1000000
    saldo_cuenta = 100000
    intentos = 0

    while True:
        usuario = input("Ingrese el usuario: ")
        clave = input("Ingrese la clave: ")

        if usuario == "10334151" and clave == "1803":
            break

        intentos += 1

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

        print("Clave inválida. Intente nuevamente.")

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_cuenta:
            if monto <= saldo_cajero:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
            else:
                print("Monto no permitido. Saldo insuficiente en el cajero.")
        else:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")

        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()

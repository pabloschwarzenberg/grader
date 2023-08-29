def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese el usuario: ")
        clave = input("Ingrese la clave: ")

        if usuario == "10334151" and clave == "1803":
            intentos = 0
            print("Bienvenido/a, usuario 10334151")
            break
        else:
            intentos += 1
            print("Clave inválida")
            if intentos == 3:
                print("Tarjeta bloqueada")
                return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_cuenta:
            if monto <= saldo_cajero:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso")
                print("Saldo cuenta=", saldo_cuenta)
                print("Saldo cajero=", saldo_cajero)
            else:
                print("Monto no permitido. Saldo insuficiente en el cajero.")
        else:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")

        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.upper() != "N":
            print("===================================")
        else:
            break


if __name__ == "__main__":
    cajero()
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido al cajero")

        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto > saldo_cuenta:
                print("Monto no permitido. Saldo insuficiente.")
            elif monto > saldo_cajero:
                print("Monto no permitido. Cajero sin suficiente dinero.")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta=", saldo_cuenta)
                print("Saldo cajero=", saldo_cajero)

            opcion = input("¿Desea hacer otro retiro? (S/N): ")
            if opcion.upper() != "S":
                break

        break
    else:
        intentos += 1
        if intentos >= 3:
            print("Tarjeta bloqueada. Demasiados intentos fallidos.")
            break
        else:
            print("Clave inválida. Intente nuevamente.")

#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido")
        saldo_inicial = saldo_cuenta
        intentos = 0

        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto > saldo_cuenta:
                print("Monto no permitido. Saldo insuficiente en la cuenta.")
            elif monto > saldo_cajero:
                print("Monto no permitido. Saldo insuficiente en el cajero.")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta:", saldo_cuenta)
                print("Saldo cajero:", saldo_cajero)

            opcion = input("Presione cualquier tecla para realizar otro retiro, o presione 'N' para salir: ")
            if opcion.upper() == "N":
                break
    else:
        intentos += 1
        print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada.")
            break

    opcion = input("Presione cualquier tecla para realizar otra operación, o presione 'N' para salir: ")
    if opcion.upper() == "N":
        break

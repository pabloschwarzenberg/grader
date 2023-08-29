saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = input("Ingrese el monto a retirar (o ingrese 'N' para salir): ")

    if monto == "N":
        break

    monto = int(monto)

    if monto <= saldo_cuenta:
        if monto <= saldo_cajero:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
        else:
            print("Monto no permitido: saldo insuficiente en el cajero")
    else:
        print("Monto no permitido: saldo insuficiente en la cuenta")

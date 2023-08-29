saldo_de_cuenta = 100000
billetes_de_20000 = 20
billetes_de_10000 = 40
billetes_de_5000 = 40
saldo_de_cajero = billetes_de_20000 * 20000 + billetes_de_10000 * 10000 + billetes_de_5000 * 5000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_de_cuenta:
        print("Monto no permitido. Fondos insuficientes en la cuenta.")
    elif monto > saldo_de_cajero:
        print("Monto no permitido. Fondos insuficientes en el cajero.")
    else:
        # Calcula la cantidad de billetes a entregar
        billetes_20000_entregados = min(monto // 20000, billetes_de_20000)
        monto -= billetes_20000_entregados * 20000

        billetes_10000_entregados = min(monto // 10000, billetes_de_10000)
        monto -= billetes_10000_entregados * 10000

        billetes_5000_entregados = min(monto // 5000, billetes_de_5000)
        monto -= billetes_5000_entregados * 5000

        saldo_de_cuenta -= (billetes_20000_entregados * 20000 +
                         billetes_10000_entregados * 10000 +
                         billetes_5000_entregados * 5000)
        saldo_de_cajero -= (billetes_20000_entregados * 20000 +
                         billetes_10000_entregados * 10000 +
                         billetes_5000_entregados * 5000)

        print("Retiro exitoso.")
        print("saldo cuenta={}".format(saldo_de_cuenta))
        print("saldo cajero={}".format(saldo_de_cajero))
        print("billetes 20000={}".format(int(billetes_20000_entregados)))
        print("billetes 10000={}".format(int(billetes_10000_entregados)))
        print("billetes 5000={}".format(int(billetes_5000_entregados)))

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion != "N":
        break
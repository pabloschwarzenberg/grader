def cajero_automatico():
    saldo_cuenta = 100000
    billetes_disponibles = {
        20000: 20,
        10000: 40,
        5000: 40
    }
    intentos = 0

    while True:
        user = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if user == "10334151" and clave == "1803":
            print("Bienvenido(a) al cajero automático.")
            break
        else:
            intentos += 1
            print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_cuenta:
            print("Saldo insuficiente en la cuenta.")
        else:
            billetes_entregados = {}
            saldo_cuenta -= monto

            for valor_billete, cantidad_billetes in billetes_disponibles.items():
                cantidad_entregada = min(int(monto / valor_billete), cantidad_billetes)
                billetes_entregados[valor_billete] = cantidad_entregada
                monto -= valor_billete * cantidad_entregada
                billetes_disponibles[valor_billete] -= cantidad_entregada

            saldo_cajero = sum(valor_billete * cantidad_billetes for valor_billete, cantidad_billetes in billetes_disponibles.items())
            print("Retiro exitoso.")
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero)
            sumabillete = sum(valor_billete * cantidad_entregada for valor_billete, cantidad_entregada in billetes_entregados.items())
            print(sumabillete)
            for valor_billete, cantidad_entregada in billetes_entregados.items():
                print("billetes " + str(valor_billete) + "=" + str(cantidad_entregada))

            break
cajero_automatico()

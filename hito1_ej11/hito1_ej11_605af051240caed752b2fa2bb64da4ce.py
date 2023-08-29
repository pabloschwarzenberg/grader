saldo_inicial = 1000000
saldo_cajero = saldo_inicial

billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}

usuarios = {
    "10334151": {
        "clave": "1803",
        "saldo": 100000
    }
}

intentos_fallidos = 0
usuario_valido = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario in usuarios and usuarios[usuario]["clave"] == clave:
        saldo = usuarios[usuario]["saldo"]
        usuario_valido = True
        break
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

if usuario_valido:
    while True:
        try:
            monto = int(input("Ingrese el monto a retirar: "))
            break
        except ValueError:
            print("Error: Entrada inválida. Intente nuevamente.")

    if monto <= 0:
        print("Monto no permitido.")
    elif monto > saldo:
        print("Saldo insuficiente.")
    elif monto > saldo_cajero:
        print("No hay suficiente dinero en el cajero.")
    else:
        billetes_entregados = {}
        monto_restante = monto

        for valor_billete, cantidad in billetes_disponibles.items():
            billetes_entregados[valor_billete] = min(cantidad, monto_restante // valor_billete)
            monto_restante -= billetes_entregados[valor_billete] * valor_billete

        if monto_restante == 0:
            for valor_billete, cantidad in billetes_entregados.items():
                billetes_disponibles[valor_billete] -= cantidad

            saldo -= monto
            saldo_cajero -= monto

            print("Saldo cuenta =", saldo)
            print("Saldo cajero =", saldo_cajero)

            for valor_billete, cantidad in billetes_entregados.items():
                if cantidad > 0:
                    print("billetes", valor_billete, "=", cantidad)
        else:
            print("No se puede retirar el monto solicitado.")

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break

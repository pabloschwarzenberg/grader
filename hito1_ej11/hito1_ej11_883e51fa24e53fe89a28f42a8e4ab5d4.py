    saldo = {20000: 20, 10000: 40, 5000: 40}

def retirar_dinero(monto):
    if monto > sum([clave * valor for clave, valor in saldo.items()]):
        print("Lo siento, no tenemos fondos suficientes para completar esta transacción")
        return

    billetes_a_entregar = {}
    for billete, cantidad in sorted(saldo.items(), reverse=True):
        billetes_a_entregar[billete] = min(monto // billete, cantidad)
        monto -= billetes_a_entregar[billete] * billete

    if monto > 0:
        print("No se puede entregar el monto solicitado con los billetes disponibles")
        return

    for billete, cantidad in billetes_a_entregar.items():
        if cantidad > 0:
            print("billetes {} = {}".format(billete, cantidad))

    for billete, cantidad in billetes_a_entregar.items():
        saldo[billete] -= cantidad  
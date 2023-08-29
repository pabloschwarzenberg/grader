def distribuir_billetes(monto):
    saldo_disponible = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    billetes_entregados = {
        20000: 0,
        10000: 0,
        5000: 0
    }

    for valor_billete, cantidad in saldo_disponible.items():
        cantidad_billetes = min(monto // valor_billete, cantidad)
        monto -= cantidad_billetes * valor_billete
        saldo_disponible[valor_billete] -= cantidad_billetes
        billetes_entregados[valor_billete] = cantidad_billetes

    if monto == 0:
        print("Retiro exitoso. Billetes entregados:")
        for valor_billete, cantidad in billetes_entregados.items():
            if cantidad > 0:
                print(str(cantidad) + " billetes de " + str(valor_billete))
    else:
        print("No es posible realizar el retiro. Saldo insuficiente o monto no válido.")
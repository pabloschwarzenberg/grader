def distribuir_billetes(monto):
    saldo = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    billetes_entregados = {}

    for denominacion, cantidad_disponible in saldo.items():
        cantidad_billetes = min(monto // denominacion, cantidad_disponible)
        billetes_entregados[denominacion] = cantidad_billetes
        monto -= denominacion * cantidad_billetes

    if monto == 0:
        for denominacion, cantidad_entregada in billetes_entregados.items():
            print("billetes {}={}".format(denominacion, cantidad_entregada))
    else:
        print("No se puede entregar la cantidad solicitada.")

# Ejemplo de uso
distribuir_billetes(45000)

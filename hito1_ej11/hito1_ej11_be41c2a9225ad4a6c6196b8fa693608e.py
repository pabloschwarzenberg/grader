saldo = {
    20000: 20,
    10000: 40,
    5000: 40
}

def distribuir_billetes(monto):
    billetes_entregados = {}
    total_entregado = 0
    for denominacion, cantidad_disponible in saldo.i, cantidad_disponible)
        billetes_entregados[denominacion] = max_entregados
        total_entregado += max_entregados * denominaciontems():
        max_entregados = min(monto // denominacion
        saldo[denominacion] -= max_entregados
        monto -= max_entregados * denominacion

    if total_entregado == monto:
        print("Retiro exitoso. Billetes entregados:")
        for denominacion, cantidad in billetes_entregados.items():
            if cantidad > 0:
                print(f,"billetes {denominacion} = {cantidad}")
        print(f"Saldo cuenta = {monto}")
        print(f"Saldo cajero = {sum(saldo.values())}")
    else:
        print("No se puede realizar el retiro. Fondos insuficientes o no se puede entregar el monto exacto.")

distribuir_billetes(50000)

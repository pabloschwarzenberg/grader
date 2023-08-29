#Cajero Automático
saldo_disponible = {
    20000: 20,
    10000: 40,
    5000: 40
}

def realizar_retiro(monto):
    if monto > sum(saldo_disponible.keys()):
        print("No hay suficiente saldo en el cajero.")
        return

    billetes_entregados = {}

    for valor_billete in sorted(saldo_disponible.keys(), reverse=True):
        cantidad_billetes = min(monto // valor_billete, saldo_disponible[valor_billete])
        if cantidad_billetes > 0:
            billetes_entregados[valor_billete] = cantidad_billetes
            monto -= cantidad_billetes * valor_billete
            saldo_disponible[valor_billete] -= cantidad_billetes

    if monto == 0:
        print("Retiro exitoso. Billetes entregados:")
        for valor_billete, cantidad in billetes_entregados.items():
        print(f"billetes {valor_billete} = {cantidad}")
        print("Saldo actual:")
        for valor_billete, cantidad in saldo_disponible.items():
            print(f"billetes {valor_billete} = {cantidad}")
    else:
        print("No es posible entregar el monto solicitado con los billetes disponibles.")
    realizar_retiro(45000)
      
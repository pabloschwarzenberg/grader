saldo = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def retirar_dinero(monto):
    global saldo, billetes_20000, billetes_10000, billetes_5000

    if monto > saldo:
        print("No hay suficiente saldo en el cajero.")
        return

    if monto % 5000 != 0:
        print("El monto debe ser múltiplo de 5000.")
        return

    if monto > (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
        print("No hay suficientes billetes en el cajero.")
        return

    # Calcular la cantidad de billetes necesarios para cada denominación
    billetes_20000_retiro = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_retiro * 20000
    billetes_10000_retiro = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_retiro * 10000
    billetes_5000_retiro = min(monto // 5000, billetes_5000)

    # Actualizar los saldos de billetes y saldo total
    billetes_20000 -= billetes_20000_retiro
    billetes_10000 -= billetes_10000_retiro
    billetes_5000 -= billetes_5000_retiro
    saldo -= (billetes_20000_retiro * 20000 + billetes_10000_retiro * 10000 + billetes_5000_retiro * 5000)

    # Imprimir los billetes entregados
    print(f"Billetes 20000 = {billetes_20000_retiro}")
    print(f"Billetes 10000 = {billetes_10000_retiro}")
    print(f"Billetes 5000 = {billetes_5000_retiro}")

    # Imprimir el saldo restante
    print(f"Saldo restante en el cajero: {saldo}")

# Ejemplo de uso
retirar_dinero(45000)
      
# Saldo inicial del cajero
saldo_cajero = {
    "billetes_20000": 20,
    "billetes_10000": 40,
    "billetes_5000": 40
}

def imprimir_saldos():
    print("Saldo actual del cajero:")
    print("Billetes de 20000:", saldo_cajero["billetes_20000"])
    print("Billetes de 10000:", saldo_cajero["billetes_10000"])
    print("Billetes de 5000:", saldo_cajero["billetes_5000"])

def realizar_retiro(monto):
    # Verificar si hay suficientes billetes para el retiro solicitado
    if monto > (saldo_cajero["billetes_20000"] * 20000 + saldo_cajero["billetes_10000"] * 10000 + saldo_cajero["billetes_5000"] * 5000):
        print("No hay suficiente saldo en el cajero para realizar el retiro.")
        return

    # Calcular la cantidad de billetes a entregar
    billetes_entregados_20000 = min(monto // 20000, saldo_cajero["billetes_20000"])
    monto -= billetes_entregados_20000 * 20000

    billetes_entregados_10000 = min(monto // 10000, saldo_cajero["billetes_10000"])
    monto -= billetes_entregados_10000 * 10000

    billetes_entregados_5000 = min(monto // 5000, saldo_cajero["billetes_5000"])
    monto -= billetes_entregados_5000 * 5000

    # Actualizar el saldo de billetes
    saldo_cajero["billetes_20000"] -= billetes_entregados_20000
    saldo_cajero["billetes_10000"] -= billetes_entregados_10000
    saldo_cajero["billetes_5000"] -= billetes_entregados_5000

    # Imprimir los saldos del cajero y el detalle de billetes entregados
    print("Saldo actual del cajero después del retiro:")
    print("Billetes de 20000:", saldo_cajero["billetes_20000"])
    print("Billetes de 10000:", saldo_cajero["billetes_10000"])
    print("Billetes de 5000:", saldo_cajero["billetes_5000"])

    print("Billetes entregados:")
    print("Billetes de 20000:", billetes_entregados_20000)
    print("Billetes de 10000:", billetes_entregados_10000)
    print("Billetes de 5000:", billetes_entregados_5000)

# Ejemplo de uso
imprimir_saldos()
realizar_retiro(20000)

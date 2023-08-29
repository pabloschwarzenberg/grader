#Cajero Automático
def withdraw(amount):
    """
    Realiza un retiro del cajero y distribuye el monto en diferentes billetes.
    """
    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40

    if amount % 5000 != 0:
        print("El monto solicitado debe ser múltiplo de 5000.")
        return
    
    total_amount = amount
    
    # Cálculo de la cantidad de billetes a entregar
    count_20000 = min(total_amount // 20000, billetes_20000)
    total_amount -= count_20000 * 20000

    count_10000 = min(total_amount // 10000, billetes_10000)
    total_amount -= count_10000 * 10000
    
    count_5000 = min(total_amount // 5000, billetes_5000)
    total_amount -= count_5000 * 5000
    
    if total_amount != 0:
        print("No hay suficientes billetes para el retiro solicitado.")
        return
    
    # Actualización de los saldos de billetes
    billetes_20000 -= count_20000
    billetes_10000 -= count_10000
    billetes_5000 -= count_5000
    
    # Impresión de los saldos y cantidad de billetes entregados
    print("Saldo actual:")
    print("Billetes de 20.000:", billetes_20000)
    print("Billetes de 10.000:", billetes_10000)
    print("Billetes de 5.000:", billetes_5000)
    print("Cantidad de billetes entregados:")
    print("Billetes de 20.000:", count_20000)
    print("Billetes de 10.000:", count_10000)
    print("Billetes de 5.000:", count_5000)
    
    # Actualización del saldo total del cajero
    saldo_cajero = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
    print("Saldo cajero:", saldo_cajero)


# Ejemplo de uso
withdraw(25000)
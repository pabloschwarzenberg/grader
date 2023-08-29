class CajeroAutomatico:
    def __init__(self):
        self.billetes_20000 = 20
        self.billetes_10000 = 40
        self.billetes_5000 = 40
        self.saldo_total = self.billetes_20000 * 20000 + self.billetes_10000 * 10000 + self.billetes_5000 * 5000

    def imprimir_saldos(self):
        print("Saldo actual:")
        print("Billetes de 20000: {0}".format(self.billetes_20000))
        print("Billetes de 10000: {0}".format(self.billetes_10000))
        print("Billetes de 5000: {0}".format(self.billetes_5000))
        print("Saldo total: {0}".format(self.saldo_total))

    def retirar_dinero(self, monto):
        if monto > self.saldo_total:
            print("No hay suficiente saldo en el cajero para realizar el retiro.")
            return
        
        billetes_20000 = min(monto // 20000, self.billetes_20000)
        monto -= billetes_20000 * 20000
        billetes_10000 = min(monto // 10000, self.billetes_10000)
        monto -= billetes_10000 * 10000
        billetes_5000 = min(monto // 5000, self.billetes_5000)
        monto -= billetes_5000 * 5000
        
        if monto > 0:
            print("No se puede entregar el monto exacto con los billetes disponibles.")
            return
        
        self.billetes_20000 -= billetes_20000
        self.billetes_10000 -= billetes_10000
        self.billetes_5000 -= billetes_5000
        self.saldo_total -= billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
        
        print("Retiro exitoso. Cantidad de billetes entregados:")
        print("Billetes de 20000: {0}".format(billetes_20000))
        print("Billetes de 10000: {0}".format(billetes_10000))
        print("Billetes de 5000: {0}".format(billetes_5000))
        
        self.imprimir_saldos()


if __name__ == "__main__":
    cajero = CajeroAutomatico()
    cajero.imprimir_saldos()
    
    while True:
        monto = int(input("Ingrese el monto a retirar (o 0 para salir): "))
        
        if monto == 0:
            break
        
        cajero.retirar_dinero(monto)

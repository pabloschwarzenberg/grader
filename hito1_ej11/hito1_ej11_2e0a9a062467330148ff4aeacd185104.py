#Cajero Automático
class CajeroAutomatico:
    def __init__(self):
        self.saldo_20000 = 20
        self.saldo_10000 = 40
        self.saldo_5000 = 40

    def retirar_dinero(self, monto):
        if monto % 5000 != 0:
            print("El monto debe ser divisible por 5000.")
            return

        billetes_20000 = min(monto // 20000, self.saldo_20000)
        monto -= billetes_20000 * 20000

        billetes_10000 = min(monto // 10000, self.saldo_10000)
        monto -= billetes_10000 * 10000

        billetes_5000 = min(monto // 5000, self.saldo_5000)
        monto -= billetes_5000 * 5000

        if monto > 0:
            print("No se puede retirar la cantidad exacta con los billetes disponibles.")
            return

        self.saldo_20000 -= billetes_20000
        self.saldo_10000 -= billetes_10000
        self.saldo_5000 -= billetes_5000

        print("Retiro exitoso.")
        print("Billetes de 20000:", billetes_20000)
        print("Billetes de 10000:", billetes_10000)
        print("Billetes de 5000:", billetes_5000)

    def imprimir_saldos(self):
        print("Saldo de billetes de 20000:", self.saldo_20000)
        print("Saldo de billetes de 10000:", self.saldo_10000)
        print("Saldo de billetes de 5000:", self.saldo_5000)


cajero = CajeroAutomatico()
cajero.imprimir_saldos()

monto_retiro = 45000
cajero.retirar_dinero(monto_retiro)

cajero.imprimir_saldos()

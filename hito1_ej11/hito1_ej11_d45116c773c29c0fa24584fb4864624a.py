class CajeroAutomatico:
    def __init__(self):
        self.billetes_20000 = 20
        self.billetes_10000 = 40
        self.billetes_5000 = 40

    def imprimir_saldos(self):
        print(f"Billetes de 20,000: {self.billetes_20000}")
        print(f"Billetes de 10,000: {self.billetes_10000}")
        print(f"Billetes de 5,000: {self.billetes_5000}")

    def retirar_dinero(self, monto):
        billetes_20000 = min(monto // 20000, self.billetes_20000)
        monto -= billetes_20000 * 20000

        billetes_10000 = min(monto // 10000, self.billetes_10000)
        monto -= billetes_10000 * 10000

        billetes_5000 = min(monto // 5000, self.billetes_5000)
        monto -= billetes_5000 * 5000

        if monto == 0:
            self.billetes_20000 -= billetes_20000
            self.billetes_10000 -= billetes_10000
            self.billetes_5000 -= billetes_5000

            print(f"Billetes de 20,000 = {billetes_20000}")
            print(f"Billetes de 10,000 = {billetes_10000}")
            print(f"Billetes de 5,000 = {billetes_5000}")
        else:
            print("No hay suficientes billetes para realizar el retiro.")
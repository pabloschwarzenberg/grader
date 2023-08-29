class CajeroAutomatico:
    def __init__(self):
        self.billetes_20000 = 20
        self.billetes_10000 = 40
        self.billetes_5000 = 40

    def imprimir_saldos(self):
        print("Saldo actual:")
        print("Billetes de 20000:", self.billetes_20000)
        print("Billetes de 10000:", self.billetes_10000)
        print("Billetes de 5000:", self.billetes_5000)

    def retirar_dinero(self, monto):
        total = monto
        billetes_20000 = min(total // 20000, self.billetes_20000)
        total -= billetes_20000 * 20000
        billetes_10000 = min(total // 10000, self.billetes_10000)
        total -= billetes_10000 * 10000
        billetes_5000 = min(total // 5000, self.billetes_5000)
        total -= billetes_5000 * 5000

        if total == 0 and billetes_20000 + billetes_10000 + billetes_5000 > 0:
            self.billetes_20000 -= billetes_20000
            self.billetes_10000 -= billetes_10000
            self.billetes_5000 -= billetes_5000

            print("Retiro exitoso")
            print("Cantidad de billetes entregados:")
            print("Billetes de 20000:", billetes_20000)
            print("Billetes de 10000:", billetes_10000)
            print("Billetes de 5000:", billetes_5000)
        else:
            print("No es posible retirar el monto solicitado")

        self.imprimir_saldos()


if __name__ == "__main__":
    cajero = CajeroAutomatico()
    cajero.imprimir_saldos()
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    cajero.retirar_dinero(monto_retiro)

class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False


if __name__ == "__main__":
    cuenta_1 = Cuenta("12864303-6", 10000)
    print("Saldo inicial de la cuenta 1:", cuenta_1.saldo)

    monto_giro = 5000
    if cuenta_1.girar(monto_giro):
        print("Giro de", monto_giro, "realizado correctamente")
    else:
        print("No es posible realizar el giro de", monto_giro)

    print("Saldo actual de la cuenta 1:", cuenta_1.saldo)

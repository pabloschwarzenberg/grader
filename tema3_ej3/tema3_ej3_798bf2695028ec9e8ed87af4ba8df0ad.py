class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        else:
            return False


if __name__ == "__main__":
    cuenta = CuentaCorriente("123456789", 50000)
    monto_giro = 30000

    if cuenta.girar(monto_giro):
        print("Giro realizado. Saldo restante: {}".format(cuenta.saldo))
    else:
        print("No es posible realizar el giro. Saldo insuficiente.")

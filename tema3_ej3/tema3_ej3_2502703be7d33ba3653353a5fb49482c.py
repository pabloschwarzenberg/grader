class CuentaCorriente:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
    cuenta_1 = self.modulo.CuentaCorriente("12864303-6",10000)
    else:
            return False


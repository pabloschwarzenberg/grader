class Cuenta:
    def init(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto > self.saldo:
            return False

        self.saldo -= monto
        return True
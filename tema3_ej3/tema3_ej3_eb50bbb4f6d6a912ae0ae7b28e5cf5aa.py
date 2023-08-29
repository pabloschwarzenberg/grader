class Cuenta:
    def init(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo
    def girar(self, monto):
        estado = False
        if monto <= self.saldo:
            estado = True
            self.saldo = self.saldo - monto
            return estado
        else:
            return estado
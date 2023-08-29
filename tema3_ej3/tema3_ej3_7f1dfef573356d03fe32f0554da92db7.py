class Cuenta:
    def __init__(self,rut,saldo):
        self.rut = rut
        self.saldo = saldo
    def girar(self,monto):
        d = self.saldo
        if self.saldo > monto:
            d -= monto
            self.saldo = d
            return True
        else:
            return False
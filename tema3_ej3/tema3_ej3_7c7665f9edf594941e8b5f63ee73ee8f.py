class Cuenta:

    def __init__(self, _rut, _saldo):
        self.rut = _rut
        self.saldo = _saldo

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        return False

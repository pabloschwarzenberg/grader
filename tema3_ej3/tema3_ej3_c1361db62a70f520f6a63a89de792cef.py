#cuenta corriente en un banco
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
# completa el código de la función
class Cuenta:
    def __init__(self, rut, saldo):
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto <= self.saldo:
            giro = True
            self.saldo = self.saldo - monto
            return giro, self.saldo
        else:
            giro = False
            return giro